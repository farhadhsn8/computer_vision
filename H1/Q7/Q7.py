import cv2
import numpy as np

img = cv2.imread('pepper.jpg')
img0 = cv2.imread('pepper.jpg')
img1 = cv2.imread('pepper.jpg')

# print(img0.shape)
img1.resize(1024, 1024,3)
img2= np.copy(img1)
# print(img.shape)

for i in range(0 , 256):
    img0 = np.delete(img0 , i , axis=0)
    img0 = np.delete(img0 , i , axis=1)

for i in range(0 , 512):
    for j in range(0 , 512):
        img1[2*i][2*j] =img[i][j]
        img1[2*i + 1][2*j]=img[i][j]
        img1[2*i][2*j+1] =img[i][j]
        img1[2*i + 1][2*j+1]=img[i][j]

img2 = cv2.resize(img, (1024,1024), interpolation=cv2.INTER_LINEAR)


cv2.imwrite('resize_0.5.jpg',img0) 
cv2.imwrite('nearest_neighbour.jpg',img1) 
cv2.imwrite('bilinear.jpg',img2) 
cv2.imwrite('linear.jpg',img2)

cv2.imshow('img',img)
cv2.imshow('img0' , img0)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey()
