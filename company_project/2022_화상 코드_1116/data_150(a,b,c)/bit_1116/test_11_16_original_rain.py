import torch
import torchvision as tv
import pandas as pd
import os 
from PIL import Image
import numpy as np 

from sklearn.metrics import accuracy_score, recall_score, precision_score, confusion_matrix
from sklearn.metrics import classification_report, f1_score

from tqdm import tqdm 
import csv

from torchvision import datasets
from src import models as models
from src import cus_dataset
import pickle
import time 


def specifi_score(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    total_n = (y_true == 0).sum()
    tn = 0
    for i in range(len(y_true)):
        if y_true[i] == 0 and y_pred[i] == 0:
            tn += 1

    return tn / total_n

def main():
    # var init 
    root_dir = '../data/data/createdata_cls/labels_2del/'
    # ['above_3rd', 'deep_2nd', 'normal', 'not_sure', 'superficial_2nd']
    # root_dir = '../data/data/con_test_211112/'
    model_path = './runs/burn_R152x2_2del_aug/best.pth' # 'runs/burn_R152x2_2del_aug/best.pth'
    model_name = 'BiT-M-R152x2'
    data_path = '../data/data/test_210914/' # test_210914_crop/'
    # data_path = '../data/data/con_test_211112/image_crop/a/' # test_210914_crop/'
    path_only = True # False
    dest_dir = './result/'
    os.makedirs(dest_dir, exist_ok=True)

    transform = tv.transforms.Compose([
        tv.transforms.Resize((512, 512)),
        tv.transforms.ToTensor(),
        tv.transforms.Normalize((0.5,), (0.5,)),
    ])
    cls_list = sorted(pd.read_csv(os.path.join(root_dir, 'cls.csv'))['cls'].tolist())
    print(os.path.join(root_dir, 'cls.csv'))
    print(cls_list)

    # load dataset & data loader
    
    if path_only:
        for cls in cls_list:
            os.makedirs(os.path.join(data_path, cls), exist_ok=True)

        dataset = datasets.ImageFolder(data_path, transform=transform)
        loader = torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=False, 
                num_workers=4, drop_last=False)
        img_list = [path[0] for path in dataset.imgs]
        print("img_list")
        print(img_list)
    else:
        # test_csv = pd.read_csv(os.path.join(root_dir, 'test.csv')) # TTEMP!!
        test_csv = pd.read_csv(os.path.join(root_dir, 'test.csv')) # TTEMP!!

        # p1 = os.path.join(root_dir, '../labels')
        p1 = root_dir
        p2 = os.path.join(root_dir, '../image_after/a')
        dataset = cus_dataset.CustomDataset(p1, p2, set_name='test', 
                cls_num=len(cls_list), transform=transform) 
        loader = torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=False, 
                num_workers=4, drop_last=False)
        img_list = test_csv['img_path'].tolist() 
    # cls_list = sorted(pd.read_csv(os.path.join(root_dir, 'labels/cls.csv'))['cls'].tolist())

    # load model
    # model = torch.load(model_path)
    model_state_dict = torch.load(model_path)
    model = models.KNOWN_MODELS[model_name](head_size=len(cls_list), zero_head=True)
    model.load_state_dict(model_state_dict['model'])
    model.eval()
    model.to('cuda:0')
    
    y_list = [] 
    pred_list = [] 
    prob_list = []
    for sample, y in tqdm(loader, desc='testing..'):
        sample = sample.cuda()
        pred = model(sample)
        prob = torch.nn.functional.softmax(pred, dim=1)
        top_p, top_class = prob.topk(1, dim=1)

        temp_pred = top_class.cpu().numpy()
        temp_pred = [prd[0] for prd in temp_pred.tolist()]
    
        temp_prob = prob.cpu().detach().numpy() # [prd for prd in prob.cpu().detach().numpy()]
        temp_prob = temp_prob.tolist()
        
        y_list.extend(y.cpu().numpy().tolist())
        pred_list.extend(temp_pred)
        prob_list.extend(temp_prob)
        
    print(y_list)
    print(pred_list)

    print(classification_report(y_list, pred_list))
    print(confusion_matrix(y_list, pred_list))

    data = {'path_list': img_list,
            'gt_list': y_list,
            'pred_list': pred_list,
            'prob_list': prob_list,
            'classes': cls_list}

    with open(os.path.join(dest_dir, 'result.pkl'), 'wb') as f:
        pickle.dump(data, f)

    print('save result in result.pkl')

if __name__ == '__main__':
    main()
