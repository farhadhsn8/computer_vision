import cv2
import numpy as np
from PIL import Image

# =====================================================================
def imadjust(x,a,b,c,d,gamma=1):
    y = (((x - a) / (b - a)) ** gamma) * (d - c) + c
    return y
# =========================================================================================================

im = Image.open("bridge2.GIF")
img = np.array(im)



img0 = img / 255
img1  = np.log(img0 + 1)

img2 = np.power(10,img0 - 1)
img3 = imadjust(img0,0.15,0.5 , 0.05 ,0.6)

img11 = img1 * 255
img22 = img2 * 255
img33 = img3 * 255
cv2.imwrite('log.jpg',img11) 
cv2.imwrite('pow.jpg',img22)
cv2.imwrite('adjust.jpg',img33) 

# print(np.min(img))
# print(np.min(img11))
# print(np.min(img22))
# print(np.min(img33))

# print(np.max(img))
# print(np.max(img11))
# print(np.max(img22))
# print(np.max(img33))

# print(np.mean(img))
# print(np.mean(img11))
# print(np.mean(img22))
# print(np.mean(img33))

print(np.std(img))
print(np.std(img11))
print(np.std(img22))
print(np.std(img33))

cv2.imshow('0',img)
cv2.imshow('normalize' , img0)
cv2.imshow('log' , img1)
cv2.imshow('pow' , img2)
cv2.imshow('adjust' , img3)
cv2.waitKey()