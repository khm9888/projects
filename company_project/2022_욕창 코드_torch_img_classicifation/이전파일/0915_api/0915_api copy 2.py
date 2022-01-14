import io
import json

from PIL import Image
from flask import Flask, jsonify, request

import argparse

import torch
import torchvision.transforms as transforms

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

# def image_crop(img,coordinate):
#     img_a = Image.open(io.BytesIO(img))
#     croppedImage=img_a.crop(coordinate)
#     return croppedImage

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
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return predicted_idx,class_index[predicted_idx]


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        # coordinate = json.load(request.data)
        coordinates = request.form.getlist('coordinate')
        
        print(coordinates)

        coordinate = [int(coord) for coord in coordinates]
        print("type(coordinate)")
        print(type(coordinate))
        # # coordinate = request.files['coordinate']
        print("coordinate")
        print(coordinate)
        class_id, class_name = get_prediction(image_bytes=img_bytes)
        result = {'cls': class_id, 'class_name': class_name}
        return jsonify(result)


if __name__ == '__main__':
    app.run(host=opt.host, port=opt.port, debug=False)