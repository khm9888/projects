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

import pdb

import datetime
date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#
year_month_day,times=date[:8],date[8:]

app = Flask(__name__)

path = f"/home/con/mmdetection/data/thyroid/test/{year_month_day}/"
# print(path)
app.config['TEST_FOLDER'] = path
cors = CORS(app, resources={r"": {"origins": "*"}})#모든 곳에서 허용


# API setting
TEST_FOLDER = path
RESULT_FOLDER = TEST_FOLDER+"/result/"
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG'])


# Initialize model
# FIXME
config = '/home/con/mmdetection/configs/_used_/cascade_rcnn_r50_fpn_fp16_2x_thyroid.py'
#checkpoint = '/mmdetection/work_dirs/cascade_rcnn_dual-res2net101_c3-c5_gcb_fpn_fp16_20e_coco/epoch_20.pth'
checkpoint = '/home/con/mmdetection/work_dirs/cascade_rcnn_r50_fpn_fp16_2x_thyroid/epoch_24.pth'
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
    if request.method == 'POST':
        # print(request.method)        
        img_files = request.files.values()
        for img_file in img_files:
            print(img_file)
            if img_file and allowed_file(img_file.filename):
                filename = secure_filename(img_file.filename)
            img_file.save(os.path.join(app.config['TEST_FOLDER'], img_file.filename))
    # print(2)
            img_filepath = os.path.join(app.config['TEST_FOLDER'], img_file.filename)
            print("img_filepath")
            print(img_filepath)

            # inference
            detect_results_np = inference_detector(model, img_filepath)
            detect_results = [ detect_result.tolist() for detect_result in detect_results_np ]

            result = {
                    'status' : 'SUCCESS',
                    'file_name' : img_file.filename,
                    'elapsed_time' : str(time.time() - st),
                    'bbox' : {classes[0]: detect_results[0],classes[1]: detect_results[1]}
                    }
            # save result 
            # FIXME : NEED TO REMOVE
            img_id = img_file.filename.split('.')[0]
            ext = img_file.filename.split('.')[1]
            new_img_id = img_id + '_detected'
            ext = ext if ext in ['jpg', 'jpeg', 'png'] else ext.lower()
            new_img_filepath = RESULT_FOLDER + new_img_id + '.' + ext 

            img = model.show_result(img_filepath, 
                    detect_results_np, 
                    score_thr=0.2, # FIXME default 0.3 
                    show=False, 
                    out_file=new_img_filepath)
            result_dict[img_file.filename]=result
            
    print(result_dict)
    return result_dict

def main():

    app.run(host='0.0.0.0', port=5005, debug=False)


if __name__ == '__main__':

    main()
