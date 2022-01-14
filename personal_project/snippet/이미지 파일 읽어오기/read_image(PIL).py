################################### 이미지 파일 읽어오기 (start) ########################

from PIL import Image
import numpy as np

img = Image.open(full_filenames[0])

# print(img.size)#(560, 482)
#출력은 (width, height)의 튜플 형태로 출력

img_np = np.array(img)
# print(img_np.shape)#(482, 560, 3)
################################### 이미지 파일 읽어오기 (end)) ########################