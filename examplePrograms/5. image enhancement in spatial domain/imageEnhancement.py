#image negative enhacement
import cv2
import numpy as np

img = cv2.imread("minions_raw.jpg",1)
gray = cv2.imread("minions_raw.jpg",0)

#creating negative image
neg = 1 - img


##############################################################################
# log transformation on image, done on gray scale image
# formula :: opPix = ScalingConst * log(1 + ipPix)
# ipPix - input pixel image
# opPix - output pixel image
# ScalingConst = 255/( log(1+max_input_pixel_value) )
# adding 1 to input pixel, since log0 = inf, and want to avoid that

#removing 0 from the image
grayNonZero = np.where( gray==0 , 1, gray)
#modified formula since 0 has been removed from the array already
ScalingConst = 255 / np.log(np.max(grayNonZero))
logImg = ScalingConst * np.log(grayNonZero)
logImg = logImg.astype(np.uint8)

##############################################################################


cv2.imshow("original image", img)
cv2.imshow("negative image", neg)
cv2.imshow("gray scale image", gray)
cv2.imshow("log transformation image", logImg)

cv2.imwrite("negativeImg.jpg", neg)
cv2.imwrite("log transformation.jpg", logImg)
cv2.waitKey(0)
cv2.destroyAllWindows()