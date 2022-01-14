"""
con
"""

import os
import json
import time
from werkzeug.utils import secure_filename
from flask import Flask, request, Response,send_file,jsonify,make_response
from flask_cors import CORS, cross_origin
import numpy as np
import base64
import argparse
import torch



import cv2

import pdb
import datetime

parser = argparse.ArgumentParser()
# parser.add_argument('--host', default='192.168.0.224')
parser.add_argument('--classifier_weights', type=str, default="/home/ubuntu/con/code/api/classifier/weights/burn_R152x2_add1/best.pth", # './classifier/weights/best.pth', 
        help='.pt file')
parser.add_argument('--host', default='127.0.0.1')
parser.add_argument('--port', default=8557)

opt, remain = parser.parse_known_args()


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#
year_month_day,times=date[:8],date[8:]

app = Flask(__name__)

# path = "/home/con/mmdetection/data/thyroid/test/{}/".format(year_month_day)
path = f"/home/ubuntu/con/test/"

app.config['TEST_FOLDER'] = path
cors = CORS(app, resources={r"": {"origins": "*"}})#모든 곳에서 허용


# API setting

TEST_FOLDER = path
RESULT_FOLDER = TEST_FOLDER+"/result/"
createFolder(RESULT_FOLDER)

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG'])


# Initialize model
# FIXME
# config = '/home/con/mmdetection/configs/_used_/cascade_rcnn_r101_fpn_fp16_2x_thyroid_1216_0.py'
#checkpoint = '/mmdetection/work_dirs/cascade_rcnn_dual-res2net101_c3-c5_gcb_fpn_fp16_20e_coco/epoch_20.pth'
# model = init_detector(config, checkpoint, )


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

"""
@app.route('/')
def hello_world():
    return 'Hello World!'
"""
@app.route('/image', methods=['POST'])
# @app.route('/train')
@cross_origin()
def image():
    return 


model = torch.load(opt.classifier_weights)
classes = list(map(str,range(6)))
# print("107")

@app.route('/', methods=['POST'])
@cross_origin()
def test():
    print()
    print("----flask print start----")
    st = time.time()
    result_dict = dict()
    # print(request.method == 'POST')
    if request.method == 'POST':
        # print(request.method)        
        img_files = request.files
        print("img_files")
        print(img_files)
        print()
        for img_file in img_files.values():
    
            print("img_file")
            print(img_file)
            print()

            print("----------")

            # pred_value = model(img_file)
            # print("---------------------")
            # print("pred_value")
            # print(pred_value)
            # print("---------------------")
                

            result = {
                    'status' : 'SUCCESS',
                    'file_name' : img_file.filename,
                    'elapsed_time' : str(time.time() - st)
                    # ,"ip":'192.168.0.181'
                    # ,"predict_result":predict_result
                    }
            
            result_dict[img_file.filename]=result

    return result_dict

def main():

    app.run(host=opt.host, port=opt.port, debug=False)


if __name__ == '__main__':

    main()
