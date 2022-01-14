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

import torch.nn.functional as F

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# 
from PIL import Image, ImageFont

from PIL import ImageDraw

# torch.cuda.empty_cache()

# choice = [1,2,3]
choice = [1]

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

######################
# 2-1. test 코드 결과
#####################

if 1 in choice:

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
        parser.add_argument("--data_num",required=True, type=int, help="data num for k-fold")

        return parser.parse_args()


        
    args = argparser(models.KNOWN_MODELS.keys())

    precrop, crop = bit_hyperrule.get_resolution_from_dataset('custom')

    test_tx = tv.transforms.Compose([
        tv.transforms.Resize((crop, crop)),
        tv.transforms.ToTensor(),
        tv.transforms.Normalize((0.5,),(0.5,))
        # tv.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), # grayscale
    ])

    test_set = cus_dataset.CustomDataset(args.datadir, args.imagedir, set_name=f'test_{args.data_num}', cls_num=6, transform=test_tx)


    # print("test_set")
    # print(test_set)

    micro_batch_size = args.batch // args.batch_split 


    test_loader = torch.utils.data.DataLoader(
        test_set, batch_size=micro_batch_size, shuffle=False,
        num_workers=args.workers, pin_memory=True, drop_last=False)

    predict_tensor=0
    true_tensor=0
    rate_list = list()
    rate_tensor=0

    # predict_tensor =predict_tensor.to(device)
    # true_tensor =predict_tensor.to(device)


    for x,y in tqdm(test_loader):
        
        model = torch.load("/home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best.pth")
        pred_value = model(x)
        # print("pred_value")
        # print(pred_value)
        pred_value = F.softmax(pred_value,dim=1)#dim 추가했으니 확인해야함.
        # print("F.softmax(pred_value, dim=0)")
        # print(max(list(F.softmax(pred, dim=0))))
        # input()
        pred = pred_value.argmax(1)
        pred_value = pred_value[0].detach().cpu().numpy()
        pred_value = max(pred_value)
        # print(pred_value)
        # pred_value = pred_value.unsqueeze(0)
        # print("pred_value")
        # print(pred_value)
        # pred_value = pred_value.detach()
        if type(predict_tensor)!=type(pred):
            predict_tensor=pred.clone()
            true_tensor=y.clone()
            rate_list.append(pred_value)
            # rate_tensor=pred_value.clone()
            # pred_value = max(pred_value.cpu().detach().numpy()[0])
            continue

        predict_tensor=torch.cat([predict_tensor,pred],dim=0)
        true_tensor=torch.cat([true_tensor,y],dim=0)
        # rate_tensor=torch.cat([rate_tensor,pred_value],dim=0)
        
        # print(f"predict_tensor: {predict_tensor}")
        # print(f"true_tensor: {true_tensor}")
        
        predict_np = predict_tensor.cpu().numpy()
        true_np = true_tensor.cpu().numpy()
        rate_list.append(pred_value)
        # rate_np = rate_tensor.detach().cpu().numpy()
        # pred_value = max(pred_value.cpu().detach().numpy()[0])
        
        # print("pred_value")
        # print(pred_value)
        # rate_np = np.append(rate_np,pred_value)
        # print(rate_np)

        # print("="*50)
        # print("predict_np")
        # print(predict_np)
        # print(len(predict_np))
        # # print("true_np")
        # # print(true_np)
        # print(len(true_np))
        # # print("rate_list")
        # # print(rate_list)
        # print(len(rate_list))
        # # print("="*50)
        # input()
        # print("rate_np")
        # print(rate_np)
        # print(len(rate_np))
    today=datetime.today().strftime("%y%m%d")


    df = pd.DataFrame({"predict" : predict_np,"true":true_np,"rate":rate_list})
    print("df")
    print(df)
    df.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/result.csv",index=0)

    dir_path = f"/home/ubuntu/con/code/BiT/data/labels/result/"
    createFolder(dir_path)
    df.to_csv(f"{dir_path}result-{args.data_num}-{today}.csv",index=0)

######################
# 2-1 완료
######################



######################
# 2-2. test 코드 결과
######################

if 2 in choice:
        
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
        # with open(f"/home/ubuntu/con/code/BiT/data/labels/result_report_{args.data_num}_{today}.txt","w") as txt_file:
        #     txt_file.write('confusion matrix\n')
        #     txt_file.write(confusion)
        #     txt_file.write("\n")
            
        #     txt_file.write("classification_report""\n")
        #     txt_file.write(classification_report(y_test, pred, target_names=target_names))
        #     txt_file.write("\n")
            
    # target_names = ['man', 'cat', 'dog']

    # y_true = [2, 0, 2, 2, 0, 1]
    # y_pred = [0, 0, 2, 2, 0, 2]

    # print(confusion_matrix(y_true, y_pred))
    # print(classification_report(y_true, y_pred, target_names=target_names))

    # get_clf_eval(y_true,y_pred,target_names)

    target_names = ['0' , '1',  '2', '3', '4', '5']
    get_clf_eval(df2["true"],df2["predict"],target_names)

######################
# 2-2 완료
######################

######################
# 2-3 result 와 test를 합치고.
######################
if 3 in choice:
        
    df_result=pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/result.csv")
    df_test=pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/test.csv")

    df_plus = pd.concat([df_result,df_test],axis=1)
    df_plus.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/result_calc.csv",index=0)

    df_plus_convert=pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/result_calc.csv")
    print(df_plus_convert)

    load_path = "/home/ubuntu/Data/Upload_file/"
    save_path = "/home/ubuntu/con/img_0901/"


    def pil_draw_rect(image, x1, y1, x2, y2,true,predict,rate):
        draw = ImageDraw.Draw(image)
        draw.rectangle(((x1, y1), (x2, y2)), outline=(255, 0, 0), width=4)
        # font = ImageFont.truetype('msyhbd.ttf',size=30)
        
        draw.text(((x1+x2)//2,(y1+y2)//2),f"true : {true}, predict :{predict}, rate: {rate:.3f}" ,(0,0,0))

        return image


    for i in range(6):
        for j in range(6):
            createFolder(f"{save_path}{i}/{j}")
    for i in tqdm(range(len(df_plus_convert))):
        file=df_plus_convert.iloc[i]['origin_path']
        cls_name=df_plus_convert.iloc[i]["true"]
        # cls_name=int(cls_name)
        predict=df_plus_convert.iloc[i]["predict"]
        x1=df_plus_convert.iloc[i]['x1']
        y1=df_plus_convert.iloc[i]['y1']
        x2=df_plus_convert.iloc[i]['x2']
        y2=df_plus_convert.iloc[i]['y2']
        rate = df_plus_convert.iloc[i]['rate']
        
        image1 = Image.open(load_path+file)
        convert_image = pil_draw_rect(image1, x1, y1, x2, y2,cls_name,predict,rate)
        convert_image=convert_image.convert('RGB')
        
        convert_image.save(f"{save_path}{cls_name}/{predict}/{file}")