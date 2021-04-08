import cv2
import numpy as np
from PIL import Image
from scipy import signal



im = Image.open("cameraman.gif") #             440 * 455
img = np.array(im)

crossL= np.array([[0,0,0],
                [0,1,0],
                [-1,0,0]])

crossR= np.array([[0,0,0],
                [0,1,0],
                [0,0,-1]])

sobelV= np.array([[-1,0,1],
                  [-2,0,2],
                  [-1,0,1]])

sobelH= np.array([[-1,-2,-1],
                  [0 , 0 , 0],
                 [ 1 , 2,  1]])

prewV= np.array([[-1,0,1],
                  [-1,0,1],
                  [-1,0,1]])

prewH= np.array([[-1,-1,-1],
                  [0 , 0 , 0],
                 [ 1 , 1,  1]])







cross_imgL = signal.convolve2d(img, crossL, boundary='symm', mode='same')
cross_imgR = signal.convolve2d(img, crossR, boundary='symm', mode='same')

sobV = signal.convolve2d(img, sobelV, boundary='symm', mode='same')
sobH = signal.convolve2d(img, sobelH, boundary='symm', mode='same')

prewittV = signal.convolve2d(img, prewV, boundary='symm', mode='same')
prewittH = signal.convolve2d(img, prewH, boundary='symm', mode='same')




print(np.shape(img))

cross_imgR= cross_imgR/255
cross_imgL= cross_imgL/255

sobH = sobH / 255
sobV = sobV / 255

prewittV = prewittV /255
prewittH = prewittH /255 

sobel_cross = np.absolute( sobV - cross_imgL )

sobel_prew = np.absolute( sobV - prewittV )

# img33/=255
# img77/=255
# img1515/=255
# cv2.imshow('norm' , img)
# cv2.imshow('3*3' , img33)
# cv2.imshow('7*7' , img77)
cv2.imshow('crossR' , cross_imgR)
cv2.imshow('crossL' , cross_imgL)

cv2.imshow('prewittH' , prewittH)
cv2.imshow('prewittV' , prewittV)

cv2.imshow('sobelV' , sobV)
cv2.imshow('sobelH' , sobH)

cv2.imshow('sobel-cross' , sobel_cross)
cv2.imshow('sobel-prew' , sobel_prew)


cross_imgR= cross_imgR*255
cross_imgL= cross_imgL*255

sobH = sobH *255
sobV = sobV * 255

prewittV = prewittV *255
prewittH = prewittH *255 

sobel_cross = sobel_cross * 255
sobel_prew  = sobel_prew  * 255


cv2.imwrite('crossR.jpg' , cross_imgR)
cv2.imwrite('crossL.jpg' , cross_imgL)

cv2.imwrite('prewittH.jpg' , prewittH)
cv2.imwrite('prewittV.jpg' , prewittV)

cv2.imwrite('sobelV.jpg' , sobV)
cv2.imwrite('sobelH.jpg' , sobH)

cv2.imwrite('sobel-cross.jpg' , sobel_cross)
cv2.imwrite('sobel-prew.jpg' , sobel_prew)



# print('1')
cv2.waitKey()



# img33*=255
# img1515*=255
# img77*=255


# cv2.imwrite('3_3.jpg',img33) 
# cv2.imwrite('15_15.jpg',img1515) 
# cv2.imwrite('7_7.jpg',img77) 

