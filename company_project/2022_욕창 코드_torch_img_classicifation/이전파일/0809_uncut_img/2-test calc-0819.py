import torch
import pandas as pd
import numpy as np
import torchvision as tv
import os

from tqdm import tqdm
from datetime import datetime
from sklearn.metrics import confusion_matrix, classification_report


from src import cus_dataset 
from src import models as models  
from src import bit_hyperrule # get resolution -> 480,  get_mixup -> 0.0 (db size < 20000),  get_schedule -> [100, 200, 300, 400, 500] (db_size < 20000), get_lr
from src import lbtoolbox as lb # Uninterrupt -> 시그널 컨트롤 (INT, TERM 등), Timer, Chrono, create_dat, load_dat 

import argparse


######################
# 2-1. test 코드 결과
#####################


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") 


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

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        



args = argparser(models.KNOWN_MODELS.keys())

precrop, crop = bit_hyperrule.get_resolution_from_dataset('custom')

test_tx = tv.transforms.Compose([
    tv.transforms.Resize((crop, crop)),
    tv.transforms.ToTensor(),
    tv.transforms.Normalize((0.5,),(0.5,))
    # tv.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), # grayscale
])

test_set = cus_dataset.CustomDataset(args.datadir, args.imagedir, set_name='test', cls_num=6, transform=test_tx)


# print("test_set")
# print(test_set)

micro_batch_size = args.batch // args.batch_split 


test_loader = torch.utils.data.DataLoader(
    test_set, batch_size=micro_batch_size, shuffle=False,
    num_workers=args.workers, pin_memory=True, drop_last=False)

predict_tensor=0
true_tensor=0
# predict_tensor =predict_tensor.to(device)
# true_tensor =predict_tensor.to(device)

for x,y in tqdm(test_loader):

    model = torch.load("/home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best.pth")
    pred = model(x).argmax(1)
    if type(predict_tensor)!=type(pred):
        predict_tensor=pred.clone()
        true_tensor=y.clone()
        continue
    predict_tensor=torch.cat([predict_tensor,pred],dim=0)
    true_tensor=torch.cat([true_tensor,y],dim=0)
    # print(f"predict_tensor: {predict_tensor}")
    # print(f"true_tensor: {true_tensor}")

    predict_np = predict_tensor.cpu().numpy()
    true_np = true_tensor.cpu().numpy()

today=datetime.today().date().strftime("%y%m%d")


df = pd.DataFrame({"predict" : predict_np,"true":true_np})
print("df")
print(df)
df.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/result.csv",index=0)

dir_path = f"/home/ubuntu/con/code/BiT/data/labels/result/"
createFolder(dir_path)
df.to_csv(f"{dir_path}result-{today}.csv",index=0)

######################
# 2-1 완료
######################



######################
# 2-2. test 코드 결과
######################

df2=pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/result.csv")
print("df2")
print(df2)

def get_clf_eval(y_test, pred,target_names):
    confusion = confusion_matrix(y_test, pred)
    print('confusion matrix')
    print(confusion)
    # accuracy = accuracy_score(y_test, pred)
    # precision = precision_score(y_test, pred)
    # recall = recall_score(y_test, pred)
    # print(f'acc : {accuracy}')
    print(classification_report(y_test, pred, target_names=target_names))

# target_names = ['man', 'cat', 'dog']
target_names = ['0' , '1',  '2', '3', '4', '5']

# y_true = [2, 0, 2, 2, 0, 1]
# y_pred = [0, 0, 2, 2, 0, 2]

# print(confusion_matrix(y_true, y_pred))
# print(classification_report(y_true, y_pred, target_names=target_names))

# get_clf_eval(y_true,y_pred,target_names)

get_clf_eval(df2["true"],df2["predict"],target_names)

######################
# 2-2 완료
######################