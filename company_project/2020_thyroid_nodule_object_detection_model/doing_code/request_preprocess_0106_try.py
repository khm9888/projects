import requests
import json
import os
import numpy as np
import pdb

import argparse
import base64 
import cv2

import datetime



classes = ["benign","malign"]
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#
year_month_day,times=date[:8],date[8:]




# img_path = '/home/con/mmdetection/data/thyroid/test/'+year_month_day+"/"
img_path = '/home/con/mmdetection/data/thyroid/test/test/'
createFolder(img_path)

filelist = os.listdir(img_path)
# filelist.sort()




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, help='.jpg', default='thyroid.jpg')
    args = parser.parse_args()

    # request send 
    # body_param = {'image': open(args.image, 'rb')}
    body_param=dict()

    for i,file in enumerate(filelist[:-1]):
        print("img_path+file")
        print(img_path+file)

        body_param[f'{file}'] = open(img_path+file,"rb")

    print("body_param")
    print(body_param)

    # req = requests.post('http://192.168.0.181:8556/extract_roi', files=body_param) # test extract_roi
    req = requests.post('http://192.168.0.181:8556/remove_marker', files=body_param) # test remove_marker
    
    print("req.text")
    print(req.text)
    print("req.text")

    # save result 
    img_data = req.text
    im_bytes = base64.b64decode(img_data)
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
    img = cv2.imdecode(im_arr, 1)

    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
    cv2.imwrite('result.jpg', img, encode_param)
