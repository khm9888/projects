import os
from os.path import join as pjoin
from typing import List
import numpy as np
from PIL import Image
from PIL import UnidentifiedImageError
import piexif
from piexif import ImageIFD


def turn_off_exif_rotation(old_path: str, image_file_name: str, new_path: str) -> np.ndarray:
    """
    To set the rotation number to 1(non-rotation), and to save an image with the rotation number 1.
    """
    old_path_name = pjoin(old_path, image_file_name)
    new_path_name = pjoin(new_path, image_file_name)
    image = Image.open(old_path_name)
    
    if 'exif' in image.info:
        exif_dict = piexif.load(image.info['exif'])
        img_orientation = ImageIFD.Orientation
        if (img_orientation in exif_dict['0th']) and exif_dict['0th'][img_orientation] != 1:
            # print(f'{image_file_name}')
            # print(f"current rotation value: {exif_dict['0th'][img_orientation]}")
            exif_dict['0th'][img_orientation] = 1
            # print('rotation value is set to 1')
            
        exif_bytes = piexif.dump(exif_dict)
        image = image.convert('RGB')  # to remove `alpha` information from `RGBA`
        image.save(new_path_name, exif=exif_bytes)
        
    else:
        image = image.convert('RGB')  # to remove `alpha` information from `RGBA`
        image.save(new_path_name)
    
    return np.array(Image.open(new_path_name))


def turn_off_exif_rotation_in_dir(old_path: str, new_path: str, images_name_list: List) -> [List, ...]:
    """
    To set the rotation number to 1, several times.
    """
    non_rot_images = []
    non_recog_images_list = []
    for name in images_name_list:
        old_path_name = pjoin(old_path, name)
        if os.path.isfile(old_path_name):
            try:
                non_rot_image = turn_off_exif_rotation(old_path, name, new_path)
                non_rot_images.append(non_rot_image)
                
            except (UnidentifiedImageError, OSError):
                print(f'{name} is unidentified!')
                non_recog_images_list.append(name)
                
    print(f'The number of unidentified images: {len(non_recog_images_list)}')
                
#     return non_rot_images, non_recog_images_list


if __name__ == '__main__':
    # example
    # old_path = pjoin('..', 'burn_raw_imgs')
    # new_path = pjoin('..', 'before_crop_data', 'non_rot_images')
    # images_name_list = sorted(os.listdir(old_path))
    # images_name_list.remove('00002883.JPG')

    # turn_off_exif_rotation_in_dir(old_path, new_path, images_name_list)