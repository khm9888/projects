"""
con
"""


classes = ["benign","malign"]

import os
import json
import time
from werkzeug.utils import secure_filename
from flask import Flask, request
from flask_cors import CORS, cross_origin
from mmdet.apis import inference_detector, init_detector
import numpy as np

import cv2

import pdb
import datetime

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#
year_month_day,times=date[:8],date[8:]

app = Flask(__name__)

path = f"/home/con/mmdetection/data/thyroid/test/{year_month_day}/"
app.config['TEST_FOLDER'] = path
cors = CORS(app, resources={r"": {"origins": "*"}})#모든 곳에서 허용


# API setting

TEST_FOLDER = path
RESULT_FOLDER = TEST_FOLDER+"/result/"
createFolder(RESULT_FOLDER)

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG'])


# Initialize model
# FIXME
config = '/home/con/mmdetection/configs/_used_/cascade_rcnn_r101_fpn_fp16_2x_thyroid_1125_0.py'
#checkpoint = '/mmdetection/work_dirs/cascade_rcnn_dual-res2net101_c3-c5_gcb_fpn_fp16_20e_coco/epoch_20.pth'
checkpoint = '/home/con/mmdetection/work_dirs/cascade_rcnn_r101_fpn_fp16_2x_thyroid_1125_0/epoch_24.pth'
device = 'cuda:0'
model = init_detector(config, checkpoint, device)

classes = ["benign","malign"]


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

"""
@app.route('/')
def hello_world():
    return 'Hello World!'
"""
@app.route('/train', methods=['POST'])
# @app.route('/train')
@cross_origin()
def train():
    return train


@app.route('/', methods=['POST'])
@cross_origin()
def test():
    print("----flask print start----")
    st = time.time()
    result_dict = dict()
    # print(request.method == 'POST')
    if request.method == 'POST':
        # print(request.method)        
        img_files = request.files


        
        for file_location,img_file in img_files.items():
            # file_name = file_location.rsplit("/")[-1]
            # path = file_location[:-len(file_name)]

            # TEST_FOLDER = path
            # RESULT_FOLDER = TEST_FOLDER+"/result/"
            # createFolder(RESULT_FOLDER)
            # app.config['TEST_FOLDER'] = path
            # print(img_file)#이 파일 확인해야함
            
            if img_file and allowed_file(img_file.filename):
                filename = secure_filename(img_file.filename)
                
            print(os.path.join(RESULT_FOLDER, img_file.filename))
            
            img_file.save(os.path.join(RESULT_FOLDER, img_file.filename))
            img_filepath = os.path.join(RESULT_FOLDER, img_file.filename)
            
            img_t=cv2.imread(img_filepath,cv2.IMREAD_COLOR)


            detect_results_np = inference_detector(model, img_t)
            detect_results = [ detect_result.tolist() for detect_result in detect_results_np ]
            
            img_id = img_file.filename.split('.')[0]
            ext = img_file.filename.split('.')[1]
            new_img_id = img_id + '_detected'
            ext = ext if ext in ['jpg', 'jpeg', 'png'] else ext.lower()
            
            new_img_filepath = RESULT_FOLDER + new_img_id + '.' + ext 
######################################################
            threshold = 0.5
            img=cv2.imread(img_filepath)
            for score in detect_results[0]:
                acc = score[-1]
                bbox = score[:-1]
                bbox=list(map(int, bbox))[:4]
                color = (255, 0, 0)#blue
                text = "benign : "+f"{acc:.2f}"
                if acc >= threshold:
                    # print(bbox)
                    img = cv2.rectangle(img, (bbox[0],bbox[1]),(bbox[2],bbox[3]), color,3)
                    x,y = int((bbox[0]+bbox[2])//2),int((bbox[1]-5))
                    cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,color,1,cv2.LINE_AA,False)
            for score in detect_results[1]:
                acc = score[-1]
                bbox = score[:-1]
                bbox=list(map(int, bbox))[:4]
                color = (0, 0, 255)#red
                text = "malign : "+f"{acc:.2f}"
                if acc >= threshold:
                    # print(bbox)
                    img = cv2.rectangle(img, (bbox[0],bbox[1]),(bbox[2],bbox[3]), color,3)
                    x,y = int((bbox[0]+bbox[2])//2),int((bbox[1]-5))
                    cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,color,1,cv2.LINE_AA,False)
                        
            cv2.imwrite(f"{new_img_filepath}",img)#id까지 표시했습니다.
######################################################
            result = {
                    'status' : 'SUCCESS',
                    # 'file_name' : img_filepath,
                    'elapsed_time' : str(time.time() - st),
                    'bbox' : {classes[0]: detect_results[0],classes[1]: detect_results[1]}
                    
                    ,"bbox_file_path": new_img_filepath
                    ,"ip":"192.168.0.181"
                    ,"port":"5005"
                    }
            # save result 
            # FIXME : NEED TO REMOVE

            # img = model.show_result(img_filepath, 
            #         detect_results_np, 
            #         score_thr=0.5, # FIXME default 0.3 
            #         show=False, 
            #         out_file=new_img_filepath)
            
            result_dict[img_filepath]=result
            
    print(result_dict)
    return result_dict

def main():

    app.run(host='0.0.0.0', port=5005, debug=False)


if __name__ == '__main__':

    main()
