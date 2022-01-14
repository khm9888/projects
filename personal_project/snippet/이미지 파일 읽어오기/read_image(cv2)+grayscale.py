# https://soyoung-new-challenge.tistory.com/112

################################### 이미지 파일 읽어오기 (start) ########################

import cv2

img = cv2.imread(full_filenames[0])
img_t = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# print(f"img.size:{img.size}")#809760 <-픽셀개수??

# print(f"img.shape:{img.shape}")#(482, 560, 3)

################################### 이미지 파일 읽어오기 (end)) ########################



################################### grayscale 적용 (start) ########################

import cv2

img_gray = cv2.imread(full_filenames[0],0)# 0dm을 추가하면 grayscale
img_t_gray = cv2.cvtColor(img_gray,cv2.COLOR_BGR2RGB)

# import matplotlib.pyplot as plt

# plt.imshow(img_t_gray)
# plt.savefig("save.png")
################################### grayscale 적용 (end) ########################
