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

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# 
from PIL import Image


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
# imagenet_class_index = json.load(open('<PATH/TO/.json/FILE>/imagenet_class_index.json'))
class_index = dict()
class_index["0"]="미분류"
class_index["1"]="1단계"
class_index["2"]="2단계"
class_index["3"]="3단계"
class_index["4"]="4단계"
class_index["5"]="심부조직손상"

precrop, crop = bit_hyperrule.get_resolution_from_dataset('custom')

# def image_crop(img,coordinate):
#     img_a = Image.open(img)
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
    print("outputs")
    print(outputs)
    # tensor([[ 1.2830,  1.5960, -0.9907, -0.4833, -1.6254,  0.2204]],
    #    device='cuda:0', grad_fn=<SelectBackward>)

    _, y_hat = outputs.max(1)
    print("y_hat")
    print(y_hat)
    # tensor([1], device='cuda:0')
    predicted_idx = str(y_hat.item())
    return predicted_idx,class_index[predicted_idx]


@app.route('/predic/t', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file'][0]
        img_bytes = file.read()
        
        # coordinate = request.coordinates["coordinate"]
        # crop_bytes = image_crop(img_bytes,coordinate)
        # class_id, class_name = get_prediction(image_bytes=crop_bytes)
        
        class_id, class_name = get_prediction(image_bytes=img_bytes)
        return jsonify({'class_id': class_id, 'class_name': class_name})


if __name__ == '__main__':
    app.run(host=opt.host, port=opt.port, debug=False)