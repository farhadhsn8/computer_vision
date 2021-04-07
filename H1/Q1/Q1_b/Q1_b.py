import cv2
img0 = cv2.imread("pepper.jpg")
img1 = cv2.imread("pepper.jpg")
#print(img0[50][50])
#print(img0.shape)



#q=256
#q=255
q=50
print(img1[256][0][0])
print(img1[100][100][1])
for i in range(0,512):
    for j in range(0,512):
        if(180>=img1[i][j][0] and img1[i][j][0]>=120):
            img1[i][j][0]=q
            img1[i][j][1]=q
            img1[i][j][2]=q
cv2.imwrite('to50.jpg',img1)  
cv2.imshow('original' , img0)
cv2.imshow('50' , img1)

cv2.waitKey()





