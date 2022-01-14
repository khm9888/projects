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
from detector import detector

import collections

parser = argparse.ArgumentParser()
parser.add_argument('--host', default='192.168.0.224')
parser.add_argument('--port', default=8556)

# detector 
parser.add_argument('--detector_device', default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
parser.add_argument('--detector_weights', type=str, default='./detector/weights/best.pt', 
        help='model.pt path(s)')
parser.add_argument('--detector_prefix', type=str, default='/detect/', help='.') 

parser.add_argument('--img-size', type=int, default=768, help='inference size (pixels)') # 800
parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
parser.add_argument('--augment', action='store_true', help='augmented inference')

# classifier
parser.add_argument('--classifier_device', type=int, default=0, help='gpu target')
parser.add_argument('--classifier_weights', type=str, default='./classifier/weights/burn_R152x2_add1/best.pth', # './classifier/weights/best.pth', 
        help='.pt file')
parser.add_argument('--classifier_prefix', type=str, default='/classify/', help='.')

# opt = parser.parse_args()
opt, remain = parser.parse_known_args()

detector_model = detector.Model(opt)
classifier_model = classifier.Model(opt)

# CLS_LIST = sorted(['normal', 'not_sure', 'superficial_2nd', 'deep_2nd', 'above_3rd'])
CLS_LIST = sorted(['normal', 'not_sure', '1st', 'superficial_2nd', 'deep_2nd', 'above_3rd'])

class BurnAPI(object):
    def __init__(self):
        app = Flask(__name__)

        cors = CORS(app, resources={r'*': {'origins': '*'}})
        app.add_url_rule(opt.detector_prefix, view_func = Detector.as_view('Detector'))
        app.add_url_rule(opt.classifier_prefix, view_func = Classifier.as_view('Classifier'))

        self.app = app
        # app.run(host=opt.host, port=opt.port,
        #         threaded=False, debug=False)
        # app.run()

class Detector(MethodView):
    def __init__(self):
        """ """
        # self.model = detector.Model(opt)
        pass

    def get(self):
        return 'not IMP'

    def post(self):
        """ """
        st_time = time.time()
        output = collections.OrderedDict({
            'elapsed_time': '',
            'status': 'FALSE',
            'coordinate': '',
        })

        # load image
        image_file = request.files['image']
        im_bytes = image_file.read()
        im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
        img = cv2.imdecode(im_arr, 1)

        try:
            # process
            # roi_img, x1, y1 = self.model.detect(img)
            x1, y1, x2, y2 = detector_model.detect(img)
            
            # return result
            output['elapsed_time'] = time.time() - st_time
            output['status'] = 'SUCCESS'
            output['coordinate'] = [x1, y1, x2, y2]
           
        except Exception as e:
            print('error : ', e)
        
        print('output : ', output)
        return json.dumps(output, ensure_ascii=False, indent='\t')


class Classifier(MethodView):
    def __init__(self):
        # self.model = classifier.Model(opt)
        pass

    def get(self):
        return 'not IMP'

    def post(self):
        st_time = time.time()
        output = collections.OrderedDict({
            'elapsed_time': '',
            'status': 'FALSE',
            'prob': '',
            'cls': '',
        })
        
        image_file = request.files['image']
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
    api = BurnAPI()
    api.app.run(host=opt.host, port=opt.port, threaded=False, debug=False)

