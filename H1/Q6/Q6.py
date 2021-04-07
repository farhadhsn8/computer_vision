import cv2
import numpy as np
from PIL import Image
from math import e


im = Image.open("skeleton.gif")
img = np.array(im)
img3=np.array(im)
# print(img.shape)

img0 = img / 255
img1 = np.power(e,img0) * 1/3
img2  = np.log(img0 + 1)

for i in range(0,800):
    for j in range(0,500):
        if(img[i][j] <= 10):
            img3[i][j] = img[i][j]
        else:
            img3[i][j]= 2 * img[i][j]


img11 = img1 * 255
img22 = img2 * 255

cv2.imwrite('e.jpg',img11) 
cv2.imwrite('log.jpg',img22)
cv2.imwrite('2x.jpg',img3) 

cv2.imshow('img',img)
cv2.imshow('img0' , img0)
cv2.imshow('img1' , img1)
cv2.imshow('img2' , img2)
cv2.imshow('img3' , img3)
cv2.waitKey()

