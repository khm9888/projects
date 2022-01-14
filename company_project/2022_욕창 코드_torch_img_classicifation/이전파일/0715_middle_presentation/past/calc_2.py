



#


"""Fine-tune a BiT model on some downstream dataset."""
import os 
from os.path import join as pjoin
import time
import numpy as np
import torch
import torchvision as tv

import random
import argparse
from src import bit_hyperrule # get resolution -> 480,  get_mixup -> 0.0 (db size < 20000),  get_schedule -> [100, 200, 300, 400, 500] (db_size < 20000), get_lr

from src import fewshot as fs # now.. pass
from src import lbtoolbox as lb  
from src import models as models  
from src import cus_logger
from src import cus_dataset 

def argparser(known_models):
    """ argparsing """
    parser = argparse.ArgumentParser(description='Fine-tune BiT-M model.')
    parser.add_argument('--name', required=True, help='Name of this run, used for monitoring.')
    parser.add_argument('--model', choices=list(known_models), help='Which variant to use; BiT-M gives best results.')
    parser.add_argument('--logdir', required=True, help='Where to log training info.')

    parser.add_argument('--pretrained_dir', default='./pretrained/', help='pretrained weights dir')
    parser.add_argument('--datadir', default='./data/', help='dataset dir') # TODO set dir
    parser.add_argument('--imagedir', default='./data/images/', help='image dir')
    parser.add_argument('--examples_per_class', type=int, default=None,
                        help='For the few-shot variant, use this many examples, per class only') # TODO 
    parser.add_argument('--examples_per_class_seed', type=int, default=0,
                        help='Random seed for selecting examples.') # TODO
    parser.add_argument('--batch', type=int, default=32, help='Batch size.') # default 512
            # 512, help='Batch size.') # default 512
    parser.add_argument('--batch_split', type=int, default=64, help='Number of batches to before update weights.') # default 1
    parser.add_argument('--base_lr', type=float, default=0.001, help='Base learning_rate for fine-tuning. In Most case default is best.')
    parser.add_argument("--workers", type=int, default=2, help="Number of background threads used to load data.")
    parser.add_argument("--eval_every", type=bool, default=True, help=".")

    return parser.parse_args()



from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix


def get_clf_eval(y_test, pred):
    confusion = confusion_matrix(y_test, pred)
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    print('confusion matrix')
    print(confusion)
    print('acc : {:.4f}\n presion : {:.4f}\n recall : {:.4f}'.format(accuracy, precision, recall))


def mktrainval(args, logger):
    """Returns train and validation datasets."""
    precrop, crop = bit_hyperrule.get_resolution_from_dataset('custom')
    train_tx = tv.transforms.Compose([
        tv.transforms.Resize((precrop, precrop)),
        tv.transforms.RandomCrop((crop, crop)),
        tv.transforms.RandomHorizontalFlip(),
        tv.transforms.ToTensor(),
        tv.transforms.Normalize((0.5,),(0.5,)) # color 
        # tv.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), # grayscale
    ])
    val_tx = tv.transforms.Compose([
        tv.transforms.Resize((crop, crop)),
        tv.transforms.ToTensor(),
        tv.transforms.Normalize((0.5,),(0.5,))
        # tv.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), # grayscale
    ])

    train_set = cus_dataset.CustomDataset(args.datadir, args.imagedir, set_name='train', cls_num=7, transform=train_tx)
    valid_set = cus_dataset.CustomDataset(args.datadir, args.imagedir, set_name='val', cls_num=7, transform=val_tx)     

    # TODO: -----------
    if args.examples_per_class is not None:
        logger.info(f"Looking for {args.examples_per_class} images per class...")
        indices = fs.find_fewshot_indices(train_set, args.examples_per_class)
        train_set = torch.utils.data.Subset(train_set, indices=indices)

    logger.info(f"Using a training set with {len(train_set)} images.")
    logger.info(f"Using a validation set with {len(valid_set)} images.")

    micro_batch_size = args.batch // args.batch_split 
    
    valid_loader = torch.utils.data.DataLoader(
        valid_set, batch_size=micro_batch_size, shuffle=False,
        num_workers=args.workers, pin_memory=True, drop_last=False)

    if micro_batch_size <= len(train_set):
        train_loader = torch.utils.data.DataLoader(
            train_set, batch_size=micro_batch_size, shuffle=True,
            num_workers=args.workers, pin_memory=True, drop_last=True)
            # drop_last=False)
    else:
        # In the few-shot cases, the total dataset size might be smaller than the batch-size.
        # In these cases, the default sampler doesn't repeat, so we need to make it do that
        # if we want to match the behaviour from the paper.
        train_loader = torch.utils.data.DataLoader(
            train_set, batch_size=micro_batch_size, num_workers=args.workers, pin_memory=True,
            sampler=torch.utils.data.RandomSampler(train_set, replacement=True, num_samples=micro_batch_size))

    return train_set, valid_set, train_loader, valid_loader

def topk(output, target, ks=(1,)):
    """Returns one boolean vector for each k, whether the target is within the output's top-k."""
    _, pred = output.topk(max(ks), 1, True, True)
    pred = pred.t()
    correct = pred.eq(target.view(1, -1).expand_as(pred))
    return [correct[:k].max(0)[0] for k in ks]

def recycle(iterable): # TODO: ??
    """ Variant of itertools.cycle that does not save iterates. """ 
    while True:
        for i in iterable:
            yield i

def run_eval(model, data_loader, device, chrono, logger, step):
    """ return loss """
    model.eval()
    
    logger.info('Running validataion...')
    logger.flush()

    all_c, all_top1 = [], [] 
    end = time.time()
    for b, (x, y) in enumerate(data_loader):
        with torch.no_grad():
            x = x.to(device, non_blocking=True)
            y = y.to(device, non_blocking=True)

            chrono._done('eval load', time.time() - end)

            with chrono.measure('eval fprop'):
                logits = model(x)
                c = torch.nn.CrossEntropyLoss(reduction='none')(logits, y)
                # get_clf_eval(y,logits)
                print(f"predict : {type(logits)}")#tensor
                print(f"true: {type(c)}")#tensor
                
                top1, top5 = topk(logits, y, ks=(1, 2)) ## TODO
                all_c.extend(c.cpu())
                all_top1.extend(top1.cpu())

        end = time.time()
    model.train()
    logger.info(f'Validation @{step} loss {np.mean(all_c):.5f}, '
                f'top1 {np.mean(all_top1):.2%} ')
    logger.flush()
    return all_c, all_top1

def mixup_data(x, y, l):
    """ Returns mixed inputs, pairs of targets, and lambda """
    indices = torch.randperm(x.shape[0]).to(x.device) # TODO randperm ??

    mixed_x = l * x + (1 - l) * x[indices]
    y_a, y_b = y, y[indices]
    return mixed_x, y_a, y_b

def mixup_criterion(criterion, pred, y_a, y_b, l):
    """ """
    return l * criterion(pred, y_a) + (1 - l) * criterion(pred, y_b)


def main(args):
    logger = cus_logger.setup_logger(args)

    # random seed fix 
    seed = 23
    print(seed)
    torch.manual_seed(seed) 
    np.random.seed(seed)
    random.seed(seed)

    # allows you to enable the inbuilt cudnn auto-tuner to find the best algorithm to use for your hardware.
    ## torch.backends.cudnn.benchmark = True 
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") 
    logger.info(f"Going to train on {device}")

    # load dataset
    train_set, valid_set, train_loader, valid_loader = mktrainval(args, logger)

    # select model
    logger.info(f"Loading model from {args.model}.npz")
    # model = models.KNOWN_MODELS[args.model](head_size=len(valid_set.classes), zero_head=True)
    # model.load_from(np.load(f"{os.path.join(args.pretrained_dir, args.model)}.npz"))
    model = torch.load("/home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best.pth")
    #con model upload

    # using all gpus 
    logger.info("Moving model onto all GPUs")
    model = torch.nn.DataParallel(model)

    # train
    # Resume from a checkpoint. Load CPU first & move the model to GPU later.
    # This way, we save a little bit of GPU memory when loading.
    step = 0

    # Note: no weight-decay!
    optim = torch.optim.SGD(model.parameters(), lr=0.003, momentum=0.9)

    saveroot = pjoin(args.logdir, args.name)
    bestname = pjoin(saveroot, 'best.pth')
    lastname = pjoin(saveroot, 'last.pth')
    # logger.info(f'model will be saved in "{savename}". ')
    
    # TODO: train resume

    model.to(device)
    optim.zero_grad()
    model.train()

    mixup = bit_hyperrule.get_mixup(len(train_set))
    cri = torch.nn.CrossEntropyLoss().to(device)
    logger.info('Starting training!')

    chrono = lb.Chrono() # measure time 

    accum_steps = 0
    mixup_l = np.random.beta(mixup, mixup) if mixup > 0 else 1 # ??
    
    end = time.time()
    
    val_metric = [99999]
    with lb.Uninterrupt() as u:
        # ex)
        # while not u.interrupted:
        #   train
        # for x, y in recycle(train_loader): # ??
        #     chrono._done('load', time.time() - end)
        #     if u.interrupted: 
        #         break 

        #     # Schedule sending to GPU(s)
        #     x = x.to(device, non_blocking=True) # ?? non_blocking ?
        #     y = y.to(device, non_blocking=True) 
            
        #     # Update learning-rate, including stop training if over
        #     lr = bit_hyperrule.get_lr(step, len(train_set), args.base_lr)
        #     if lr is None:
        #         break
        #     for param_group in optim.param_groups:
        #         param_group['lr'] = lr

        #     if mixup > 0.0: # 0.0 if data < 20_000
        #         x, y_a, y_b = mixup_data(x, y, mixup_l) 

        #     # Compute output
        #     with chrono.measure('fprop'): 
        #         logits = model(x)
        #         if mixup > 0.0:
        #             c = mixup_criterion(cri, logits, y_a, y_b, mixup_l)
        #         else:
        #             c = cri(logits, y)
        #         c_num = float(c.data.cpu().numpy()) # TODO: Also ensures a sync point

        #     # accumulate grads 
        #     with chrono.measure('grads'):
        #         (c / args.batch_split).backward() 
        #         accum_steps += 1
        
        #     accstep = f'({accum_steps}/{args.batch_split})' if args.batch_split > 1 else ''
        #     logger.info(f'[step {step}{accstep}]: loss={c_num:.5f} (lr={lr:.1e})')
        #     logger.flush()

        #     # Update params
        #     if accum_steps == args.batch_split:
        #         with chrono.measure('update'):
        #             optim.step()
        #             optim.zero_grad()
        #         step += 1
        #         accum_steps = 0
        #         # Sample new mixup ratio for next batch 
        #         mixup_l = np.random.beta(mixup, mixup) if mixup > 0 else 1

        #         # Run eval and save model
        #         if args.eval_every and step % 10 == 0:
        #             all_c, all_top1 = run_eval(model, valid_loader, device, chrono, logger, step)
        #             torch.save(model, lastname)# savename)
        #             # save best 
        #             cur_metric = np.mean(all_c)
        #             if cur_metric <= max(val_metric):
        #                 torch.save(model, bestname)
        #                 val_metric.append(np.mean(all_c))
        #         end = time.time()
        
        # Final eval at end of training 
        all_c, all_top1 = run_eval(model, valid_loader, device, chrono, logger, step)
        """
        torch.save({'step': step, 
                    'model': model.state_dict(), 
                    'optim': optim.state_dict(),}, lastname) 
        """
        torch.save(model, lastname)
        # save best 
        cur_metric = np.mean(all_c)
        if cur_metric <= min(val_metric):
            torch.save(model, bestname)
            val_metric.append(np.mean(all_c))
        
        logger.info(f'Timings:\n{chrono}')

if __name__ == "__main__":
    args = argparser(models.KNOWN_MODELS.keys())
    main(args)

