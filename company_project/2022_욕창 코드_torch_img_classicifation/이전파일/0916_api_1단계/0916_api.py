import io
import json
import time

from PIL import Image
from flask import Flask, jsonify, request

import argparse

import torch
import torchvision.transforms as transforms
import torch.nn.functional as F


from src import cus_dataset 
from src import models as models  
from src import bit_hyperrule # get resolution -> 480,  get_mixup -> 0.0 (db size < 20000),  get_schedule -> [100, 200, 300, 400, 500] (db_size < 20000), get_lr
from src import lbtoolbox as lb # Uninterrupt -> 시그널 컨트롤 (INT, TERM 등), Timer, Chrono, create_dat, load_dat 

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") 

parser = argparse.ArgumentParser()
# parser.add_argument('--host', default='192.168.0.224')
# parser.add_argument('--classifier_weights', type=str, default="/home/ubuntu/con/code/api/classifier/weights/burn_R152x2_add1/best.pth", # './classifier/weights/best.pth', 
parser.add_argument('--classifier_weights', type=str, default="/home/ubuntu/con/code/api/classifier/weights/burn_R152x2_add1/best.pth", # './classifier/weights/best.pth', 
        help='.pt file')
parser.add_argument('--host', default='127.0.0.1')
parser.add_argument('--port', default=8557)

opt, remain = parser.parse_known_args()

print("opt.classifier_weights")
print(opt.classifier_weights)
model = torch.load(opt.classifier_weights)
model.eval()


app = Flask(__name__)

class_index = dict()
class_index["0"]="unstageable"
class_index["1"]="stage 1"
class_index["2"]="stage 2"
class_index["3"]="stage 3"
class_index["4"]="stage 4"
class_index["5"]="suspected_deep_tissue_injury"

precrop, crop = bit_hyperrule.get_resolution_from_dataset('custom')

def image_to_byte_array(image):

    imgByteArr = io.BytesIO()
    image.save(imgByteArr,"PNG")
    imgByteArr = imgByteArr.getvalue()

    return imgByteArr

def image_crop(img_bytes,coordinate):
    img_a = Image.open(io.BytesIO(img_bytes))
    croppedImage=img_a.crop(coordinate)

    return image_to_byte_array(croppedImage)

def transform_image(image_bytes):
    my_transforms = transforms.Compose([
        transforms.Resize((crop, crop)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,),(0.5,))])
    
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    # print("outputs")
    # print(outputs)
    # print()
    probs = F.softmax(outputs,dim=1)
    probs_np = probs.cpu().detach().numpy()[0]
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    prob = probs_np[int(predicted_idx)]
    prob = float(prob)

    return predicted_idx,class_index[predicted_idx],prob


@app.route('/predict', methods=['POST'])
def predict():
    print("----flask print start----")
    st = time.time()
    if request.method == 'POST':
        file = request.files['file']

        img_bytes = file.read()
        coordinates = request.form.getlist('coordinate')
        coordinate = [int(coord) for coord in coordinates]
        
        img_bytes=image_crop(img_bytes,coordinate)

        class_id, class_name, prob = get_prediction(image_bytes=img_bytes)
        result = {'cls_no': class_id, 
                  'cls': class_name,
                  "prob" : prob,
                #   'elapsed_time' : str(time.time() - st)
                  'elapsed_time' : time.time() - st
                  }
        print(result)
        for v in result.values():
            print(v,type(v))
        return jsonify(result)


if __name__ == '__main__':
    app.run(host=opt.host, port=opt.port, debug=False)