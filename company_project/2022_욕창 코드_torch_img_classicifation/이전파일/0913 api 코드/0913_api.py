import sys 
sys.path.append('./classifier/')
sys.path.append('./detector/')

import argparse
import time
import os
import json

import cv2
import torch
import numpy as np
import base64

from flask import Flask
from flask import request
from flask.views import MethodView
from flask_cors import CORS

from classifier import classifier

import collections

parser = argparse.ArgumentParser()
# parser.add_argument('--host', default='192.168.0.224')
parser.add_argument('--host', default='127.0.0.1')
parser.add_argument('--port', default=8557)


# parser.add_argument('--img-size', type=int, default=768, help='inference size (pixels)') # 800
# parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
# parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
# parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
# parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
# parser.add_argument('--augment', action='store_true', help='augmented inference')

# classifier
parser.add_argument('--classifier_device', type=int, default=0, help='gpu target')
parser.add_argument('--classifier_weights', type=str, default="/home/ubuntu/con/code/api/classifier/weights/burn_R152x2_add1/best.pth", # './classifier/weights/best.pth', 
        help='.pt file')
parser.add_argument('--classifier_prefix', type=str, default='/classify/', help='.')

# opt = parser.parse_args()
opt, remain = parser.parse_known_args()

classifier_model = classifier.Model(opt)

# CLS_LIST = sorted(['normal', 'not_sure', 'superficial_2nd', 'deep_2nd', 'above_3rd'])
CLS_LIST = sorted(range(6))

class BedsoreAPI(object):
    def __init__(self):
        app = Flask(__name__)

        cors = CORS(app, resources={r'*': {'origins': '*'}})
        app.add_url_rule(opt.classifier_prefix, view_func = Classifier.as_view('Classifier'))

        self.app = app
        # app.run(host=opt.host, port=opt.port,
        #         threaded=False, debug=False)
        # app.run()

class Classifier(MethodView):
    def __init__(self):
        print(0)
        # self.model = classifier.Model(opt)
        pass

    def get(self):
        print("2")
        
        return 'not IMP'

    def post(self):
        print("3")
        
        st_time = time.time()
        print("st_time")
        print(st_time)
        output = collections.OrderedDict({
            'elapsed_time': '',
            'status': 'FALSE',
            'prob': '',
            'cls': '',
        })
        
        print("request")
        print(request)
        for image_file in request.files.values():
            print(image_file)
            im_bytes = image_file.read()

            coordinate = request.form.getlist('coordinate')
            coordinate = [int(coord) for coord in coordinate]
            
            with torch.no_grad():
                # TODO: image size 
                pred = classifier_model.classify(im_bytes, coordinate)
                prob = torch.nn.functional.softmax(pred, dim=1)
                top_p, top_class = prob.topk(1, dim=1)
                top_p = top_p.cpu().numpy().tolist()[0][0]
                top_class = top_class.cpu().numpy().tolist()[0][0]

                output['elapsed_time'] = time.time() - st_time
                output['status'] = 'SUCCESS'
                output['prob'] = top_p
                output['cls'] = CLS_LIST[top_class]

            print(output)
        return json.dumps(output, ensure_ascii=False, indent='\t')


if __name__ == '__main__':
    api = BedsoreAPI()
    # api.app.run(host=opt.host, port=opt.port, threaded=False, debug=False)
    api.app.run(host=opt.host, port=opt.port, debug=True)
    print("1")
    # api.app.run(host='0.0.0.0', port=opt.port, threaded=False, debug=False)
    # api.app.run(host='10.10.11.181', port=opt.port, threaded=False, debug=False)

@app.route('/', methods=['POST'])
@cross_origin()
def test():
    img_files = request.files     
    for file_location,img_file in img_files.items():

        
        if img_file and allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
            
        print(os.path.join(RESULT_FOLDER, img_file.filename))
