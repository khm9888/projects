import os
import torch
import numpy as np
import pandas as pd 
from torch.utils.data import Dataset, DataLoader
# import cv2
from PIL import Image 

class CustomDataset(Dataset):
    def __init__(self, root_dir, image_dir, cls_num=2, set_name='data', transform=None):
        """
            root_dir (str) : root_dir/..., root_dir/images/image_file..
            set_name (str) : set_name (train, val)..
            transform (callable, optional) : optional transform to be applied on a sample..
        """
        self.root_dir = root_dir
        self.image_dir = image_dir
        self.set_name = set_name

        self.csv_path = os.path.join(self.root_dir, f'{set_name}.csv')
        self.cls_path = os.path.join(self.root_dir, 'cls.csv')
        self.transform = transform

        self.image_ids, self.labels, self.classes = self.load_csv()

        """
        self.image_ids = self.image_ids[:1009]
        self.labels = self.labels[:1009]
        self.classes = self.classes[:1009]
        """
        self.cls_num = len(self.classes)

    def __len__(self):
        return len(self.image_ids)

    def __getitem__(self, idx):
        img = self.load_image(idx)
        annot = self.load_annotations(idx)
        if self.transform:
            sample = self.transform(img)
        return sample, annot

    def load_csv(self):
        data = pd.read_csv(self.csv_path)
        # paths = data['path'].tolist()
        paths = data['img_path'].tolist()
        labels = data['cls'].tolist()

        data = pd.read_csv(self.cls_path)
        # classes = data['cls'].tolist() 
        classes = sorted(data['cls'].tolist())
        return paths, labels, classes

    def load_image(self, image_index): 
        path = os.path.join(self.image_dir, self.image_ids[image_index])
        img = Image.open(path).convert('RGB')
        return img

    def load_annotations(self, image_index):
        label = self.labels[image_index]
        label = self.classes.index(label) # ++
        label = torch.tensor(label, dtype=torch.long)
        return label
