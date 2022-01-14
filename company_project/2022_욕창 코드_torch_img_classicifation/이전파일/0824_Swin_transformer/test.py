import os
from os.path import join as pjoin
import time
import argparse
import datetime
import numpy as np
import yaml
from glob import glob 
from PIL import Image
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
import pickle
from tqdm import tqdm

import torch
from torchvision import datasets

from models import build_model
from utils import load_checkpoint_for_api
from data.build import build_transform


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--classifier_device', default='0')
    parser.add_argument('--classifier_cfg', default="/home/ubuntu/Swin-Transformer/out/swin_all_test/swin_large_patch4_window7_224/default/config.json")
    # parser.add_argument('--classifier_cfg', default='./out/swin_all/swin_large_patch4_window7_224/default/config.json')
    parser.add_argument('--classifier_weights', default='/home/ubuntu/Swin-Transformer/out/swint_original_l_pretrained/swin_large_patch4_window7_224/default/ckpt_epoch_best.pth')
    # parser.add_argument('--classifier_weights', default='./out/swin_all/swin_large_patch4_window7_224/default/ckpt_epoch_best.pth')
    parser.add_argument('--data-path')
    # parser.add_argument('--data_path', default='/home/lab/rain/template/projects/burn/send_data/data/swint_cls_form_ori/test/')
    args = parser.parse_args()

    return args

class Model:
    def __init__(self, opt):
        """ """
        self.device = torch.device(f'cuda:{opt.classifier_device}')
        self.weights = opt.classifier_weights
        self.cfg = opt.classifier_cfg
        
        self.config = self.load_cfg()
        self.load_model()
        self.transform = build_transform(False, self.config)

    def load_cfg(self):
        with open(self.cfg, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        config['MODEL']['RESUME'] = self.weights
        return config

    def load_model(self):
        self.model = build_model(self.config)
        self.model.to(self.device)
        load_checkpoint_for_api(self.config, self.model)
        self.model.eval()
    
    def classify(self, im_bytes, coordinate):
        img = Image.open(BytesIO(im_bytes)).convert('RGB')
        width, height = img.size
        x1, y1, x2, y2 = coordinate

        if x1 < 0:
            x1 = 0 
        if y1 < 0:
            y1 = 0
        if x2 > width or x2 == -1:
            x2 = width
        if y2 > height or y2 == -1:
            y2 = height

        img = img.crop((x1, y1, x2, y2))
        
        sample = self.transform(img).cuda()
        sample = sample.unsqueeze(0)

        res = self.model(sample)
        return res


def main():
    opt = parse_args()
    swin = Model(opt)
    
    dataset = datasets.ImageFolder(opt.data_path, transform=swin.transform)
    loader = torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=False, num_workers=4)
    print(dataset.classes)
    img_list = [path[0] for path in dataset.imgs]

    # test!
    y_list = []
    pred_list = []
    prob_list = []
    for sample, y in tqdm(loader, desc='testing..'):
        sample = sample.cuda()
        pred = swin.model(sample)
#        print('pred')
#        print(pred)       
        prob = torch.nn.functional.softmax(pred, dim=1)
        top_p, top_class = prob.topk(1, dim=1)

        temp_y = y.cpu().numpy().tolist()
        
        temp_pred = top_class.cpu().numpy()
#        print('temp_pred')        
#        print(temp_pred)
        temp_pred = [p[0] for p in temp_pred.tolist()]
#        print('temp_pred')        
#        print(temp_pred)
        temp_prob = prob.cpu().detach().numpy()
        temp_prob = temp_prob.tolist()[0]

#        print('temp_prob')
#        print(temp_prob)

#        input()

        y_list.extend(temp_y)
        pred_list.extend(temp_pred)
        prob_list.extend(temp_prob)

    # print(y_list)
    # print(pred_list)
    # print(prob_list)

    print(classification_report(y_list, pred_list))
    print(confusion_matrix(y_list, pred_list))
#    print(f1_score(y_list, pred_list))

    data = {'path_list': img_list,
            'gt_list': y_list,
            'pred_list': pred_list,
            'prob_list': prob_list,
            'classes': dataset.classes}
    with open('result.pkl', 'wb') as f:
        pickle.dump(data, f)
    
    print('save result in result.pkl')

if __name__ == '__main__':
    main()
