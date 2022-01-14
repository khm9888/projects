import io
import json
import time

from PIL import Image
from flask import Flask, jsonify, request

import argparse

import torch
import torchvision.transforms as transforms
import torch.nn.functional as F


# from src import cus_dataset 
# from src import models as models  
# from src import bit_hyperrule # get resolution -> 480,  get_mixup -> 0.0 (db size < 20000),  get_schedule -> [100, 200, 300, 400, 500] (db_size < 20000), get_lr
# from src import lbtoolbox as lb # Uninterrupt -> 시그널 컨트롤 (INT, TERM 등), Timer, Chrono, create_dat, load_dat 

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") 

parser = argparse.ArgumentParser()
# parser.add_argument('--host', default='192.168.0.224')
# parser.add_argument('--classifier_weights', type=str, default="/home/ubuntu/con/code/api/classifier/weights/burn_R152x2_add1/best.pth", # './classifier/weights/best.pth', 
parser.add_argument('--classifier_weights', type=str, default="/home/ubuntu/con/code/api/classifier/weights/burn_R152x2_add1/best.pth", # './classifier/weights/best.pth', 
        help='.pt file')
parser.add_argument('--host', default='0.0.0.0')
parser.add_argument('--port', default=65281)

opt, remain = parser.parse_known_args()


app = Flask(__name__)

code_list = list(range(1001,1011))


@app.route('/dressing', methods=['POST'])
def predict():
    print("----flask print start----")
    st = time.time()
    if request.method == 'POST':
        datas = request.form
        print("datas")
        print(datas)
        condition1=datas["c1"]
        condition2=datas["c2"]
        condition3=datas["c3"]
        condition4=datas["c4"]
        cls_no = int(datas["cls_no"])
        print("condition1")
        print(condition1)
        print("condition2")
        print(condition2)
        if condition1:
            if condition2:
                if cls_no >3:
                    code = 1005
                else:
                    code =1007
            else: 
                code = 1003
        else:
            code = 1002
            
        print(66)
            
        # code = 1000
                    
        result = {'code': code, 
                'elapsed_time' : time.time() - st
                    
                    }
        print(result)
        # for v in result.values():
        #     print(v,type(v))
        return jsonify(result)


if __name__ == '__main__':
    app.run(host=opt.host, port=opt.port, debug=False)