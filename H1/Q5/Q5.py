import cv2
import numpy as np
from PIL import Image



im = Image.open("hw1sp2012Prob2.gif")
img = np.array(im)
rot = im.rotate(60)
rot0 = np.array(rot)
img1 = np.array(im)
# cv2.imshow('norm',img)
cv2.imshow('norm1',img1)
# cv2.imshow('norm',rot0)
for i in range(39,80):
    for j in range(39,80):                                  #39   79
        img1[i+40][j+40] = img[i][j]                       # 239  379
        img1[i][j] = 0

for i in range(90,512):
    for j in range(100,512):
        img[i][j] = 0
        img[i][j] = rot0[i][j] 

        
cv2.imwrite('rotate.jpg',img) 
cv2.imwrite('trans.jpg',img1) 
cv2.imwrite('tmp.jpg',rot0) 
cv2.imshow('trans_x,y',img1)
cv2.imshow('rotate',img)
cv2.waitKey()