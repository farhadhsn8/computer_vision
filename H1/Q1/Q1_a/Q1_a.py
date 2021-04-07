import cv2
img0 = cv2.imread("pepper.jpg")
img1 = img0 + 50
cv2.imwrite('plus50.jpg',img1)

cv2.imshow('original' , img0)
cv2.imshow('+50' , img1)
cv2.waitKey()





