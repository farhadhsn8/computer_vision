import cv2
import numpy as np
from PIL import Image, ImageOps 
from scipy import signal




#=========================================================
def salt_and_pepper(arr, prob=0.05):
    # If the specified `prob` is negative or zero, we don't need to do anything.
    if prob <= 0:
        return image

    # arr = np.asarray(Image.fromarray(salt_and_peppered_arr))
    original_dtype = arr.dtype

    intensity_levels = 2 ** (arr[0, 0].nbytes * 8)

    min_intensity = 0
    max_intensity = intensity_levels - 1

    
    random_image_arr = np.random.choice(
        [min_intensity, 1, np.nan], p=[prob / 2, 1 - prob, prob / 2], size=arr.shape
    )

   
    salt_and_peppered_arr = arr.astype(np.float) * random_image_arr

   
    salt_and_peppered_arr = np.nan_to_num(
        salt_and_peppered_arr, nan=max_intensity
    ).astype(original_dtype)
    arr = np.asarray(Image.fromarray(salt_and_peppered_arr))
    return arr

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
#===================================================================

im = Image.open("pepper.jpg")
im = ImageOps.grayscale(im) 


img = np.array(im)

# print(np.shape(img))

sp = salt_and_pepper(img,0.2)

kernel33 =(1/9)* np.ones((3,3))



img33 = signal.convolve2d(img, kernel33, boundary='symm', mode='same')
sec33 = signal.convolve2d(img33, kernel33, boundary='symm', mode='same')

median1 = median(sp, 512,512,3)
median2 = median(median1, 512,512,3)

img33/=255
sec33/=255
median1/=255
median2/=255



cv2.imshow('norm' , img)
cv2.imshow('3 * 3' , img33)
cv2.imshow('3 * 3 second' , sec33)
cv2.imshow('sp_img' , sp)
cv2.imshow('median1' , median1)
cv2.imshow('sec_median' , median2)


img33*=255
sec33*=255
median1*=255
median2*=255


cv2.imwrite('avg33.jpg' , img33)
cv2.imwrite('second_avg33.jpg' , sec33)
cv2.imwrite('sp.jpg' , sp)
cv2.imwrite('median1.jpg' , median1)
cv2.imwrite('median2.jpg' , median2)


# img33*=255
# img55*=255
# img77*=255
# img_sharpen*=255
# img_sharpen2*=255

# cv2.imwrite('33.jpg',img33) 
# cv2.imwrite('55.jpg',img55) 
# cv2.imwrite('77.jpg',img77) 
# cv2.imwrite('sharpen.jpg',img_sharpen) 
# cv2.imwrite('sharpen2.jpg',img_sharpen2) 

cv2.waitKey()
