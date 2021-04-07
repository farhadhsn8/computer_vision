import cv2
import numpy as np

img0 = cv2.imread("pepper.jpg")
img1  = img0/255

print(img1.shape)
# print(img1)

img1 = np.log(img1 + 1)

# print(img1)
img2=img1*255
cv2.imwrite('log10.jpg',img2)  

cv2.imshow('original' , img0)
cv2.imshow('log10' , img1)
cv2.waitKey()

