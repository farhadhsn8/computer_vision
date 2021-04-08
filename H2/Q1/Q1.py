import cv2
import numpy as np
from PIL import Image
from scipy import signal


im = Image.open("bridge.gif")
img = np.array(im)



kernel33 =(1/9)* np.ones((3,3))
kernel55 =(1/25)* np.ones((5,5))
kernel77 =(1/49)* np.ones((7,7))

sharpen = np.array([[0,-1,0],
                    [-1,5,-1],
                    [0,-1,0]])


img33 = signal.convolve2d(img, kernel33, boundary='symm', mode='same')
img55 = signal.convolve2d(img, kernel55, boundary='symm', mode='same')
img77 = signal.convolve2d(img, kernel77, boundary='symm', mode='same')
img_sharpen = signal.convolve2d(img33, sharpen, boundary='symm', mode='same')
img_sharpen2 = signal.convolve2d(img_sharpen, sharpen, boundary='symm', mode='same')


img33/=255
img55/=255
img77/=255
img_sharpen/=255
img_sharpen2/=255

cv2.imshow('norm' , img)
cv2.imshow('3 * 3' , img33)
cv2.imshow('5 * 5' , img55)
cv2.imshow('7 * 7' , img77)
cv2.imshow('sharpen' , img_sharpen)
cv2.imshow('sharpen2' , img_sharpen2)




img33*=255
img55*=255
img77*=255
img_sharpen*=255
img_sharpen2*=255

cv2.imwrite('33.jpg',img33) 
cv2.imwrite('55.jpg',img55) 
cv2.imwrite('77.jpg',img77) 
cv2.imwrite('sharpen.jpg',img_sharpen) 
cv2.imwrite('sharpen2.jpg',img_sharpen2) 

cv2.waitKey()
