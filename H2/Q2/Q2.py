import cv2
import numpy as np
from PIL import Image
from scipy import signal

def med(a,n):
    b=np.sort(a, axis=None) 
    # print(b)
    return b[n**2 // 2]


def median(pic ,w,h, n):
    a=np.zeros((n,n))
    newpic=np.zeros((w,h))
    for i in range(n//2,w-(n//2)):
        for j in range(n//2,h-(n//2)):
            for k in range(0,n):
                for l in range(0,n):
                    a[k,l]=pic[(i-(n//2))+k][(j-(n//2))+l]
            newpic[i][j]=med(a,n)
    return newpic





im = Image.open("Q2.tif") #             440 * 455
img = np.array(im)

img33= median(img,440 , 455 , 3)
img77= median(img,440 , 455 , 7)
img1515= median(img,440 , 455 , 15)

img33/=255
img77/=255
img1515/=255
cv2.imshow('norm' , img)
cv2.imshow('3*3' , img33)
cv2.imshow('7*7' , img77)
cv2.imshow('15*15' , img1515)
print('1')
cv2.waitKey()



img33*=255
img1515*=255
img77*=255


cv2.imwrite('3_3.jpg',img33) 
cv2.imwrite('15_15.jpg',img1515) 
cv2.imwrite('7_7.jpg',img77) 

