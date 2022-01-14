import cv2
import numpy as np
import os
import time

# import matplotlib.pyplot as plt


img_path = "/home/con/mmdetection/data/thyroid/data/"
# img_path = "/mnt/sdb/AI/work/check_img/"
# save_mask_path = "/mnt/sdb/AI/work/mask/"
save_img_path = "/mnt/sdb/AI/work/mask/"

file_list = os.listdir(f"{img_path}")

# print(file_list)

# file=file_list[0]
name="2020-10-22_06_17_01"
file=name+".jpg"
print(file)


img = cv2.imread(img_path+file)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

time.sleep(1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("gray",gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ret, mask = cv2.threshold(gray, 224, 255, cv2.THRESH_BINARY)#1
# ret, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)#백을 마스크
ret, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV)#흑을 마스크
cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.Bin)

cv2.imshow('mask0',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

time.sleep(1)

ret, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)#백을 마스크

cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

time.sleep(1)

# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow('gray',gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

dst = cv2.inpaint(img,mask,5,cv2.INPAINT_NS)


cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# time.sleep(1)

# gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

# ret, mask = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY_INV)#흑을 마스크

# cv2.imshow('mask',mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# dst = cv2.inpaint(img,mask,3,cv2.INPAINT_NS)

# cv2.imshow("dst",dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()