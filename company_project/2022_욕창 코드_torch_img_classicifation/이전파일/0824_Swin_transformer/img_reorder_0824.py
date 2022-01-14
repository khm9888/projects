#/home/ubuntu/con/code/BiT/data <- cut 이미지가 있다는 전제하에.
import pandas as pd
from PIL import Image
import os
from tqdm import tqdm


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
    
def reorder(file,i):
    img_path = "/home/ubuntu/Swin-Transformer/data/images_cut/"
    save_path = "/home/ubuntu/Swin-Transformer/data/images/"
    data_df = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/{file}.csv")

    data_df_0=data_df[data_df["cls"]==i]

    for img in tqdm(data_df_0["img_path"]):
        image1 = Image.open(f"{img_path}{img}")
  
        image1.save(f"{save_path}{file[:-2]}/{i}/{img}")

path = "/home/ubuntu/Swin-Transformer/data/images/"
path_train=path+"train/"
path_val=path+"val/"
path_test=path+"test/"
createFolder(path_test)
for i in range(6):
    createFolder(path_train+f"{str(i)}/")
    createFolder(path_val+f"{str(i)}/")
    createFolder(path_test+f"{str(i)}/")
for i in range(6):
    reorder("train_0",i)
    reorder("val_0",i)
    reorder("test_0",i)


