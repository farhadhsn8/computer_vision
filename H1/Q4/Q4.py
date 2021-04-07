import cv2
import numpy as np
from PIL import Image



im = Image.open("building1.gif")
img = np.array(im)

cv2.imshow('0',img)

print(np.min(img))
print(np.max(img))
print(np.mean(img))
print(np.median(img))
print(np.std(img))

cnt=0
for i in range(0,512):
    for j in range(0,512):
        if(img[i][j]==128):
            cnt+=1
           
print(cnt)
print('=======================================')
img0=img + 50

cv2.imshow('50',img0)

print(np.min(img0))
print(np.max(img0))
print(np.mean(img0))
print(np.median(img0))
print(np.std(img0))

cnt=0
for i in range(0,512):
    for j in range(0,512):
        if(img0[i][j]==128):
            cnt+=1
           
print(cnt)

cv2.imwrite('plus50.jpg',img0) 

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

img1=(255/(np.max(img)-np.min(img))) * (img - np.min(img))
img1 = img1 / 256 
cv2.imshow('g',img1)
img1 = img1 * 256 
print(np.min(img1))
print(np.max(img1))
print(np.mean(img1))
print(np.median(img1))
print(np.std(img1))

cnt=0
for i in range(0,512):
    for j in range(0,512):
        if(img1[i][j]==128):
            cnt+=1
           
print(cnt)

cv2.imwrite('g.jpg',img1) 
cv2.waitKey()
