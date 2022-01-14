import cv2
import numpy as np
import matplotlib.pyplot as plt


img_path = "/inpaint_code/images/"

img = cv2.imread(img_path+'8.jpg')
cv2.imshow(img,'gray')
plt.axis('off')
plt.savefig(img_path+'8_2.jpg')

noise = cv2.imread(img_path+'/8.jpg',0)
noise = cv2.resize(noise,(img.shape[1],img.shape[0]))
print(noise.shape == img.shape)
plt.imshow(noise,'gray')
plt.axis('off')
plt.savefig(img_path+'8_gray.jpg')