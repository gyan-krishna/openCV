#image negative enhacement
import cv2
import numpy as np

img = cv2.imread("minions_raw.jpg",1)
gray = cv2.imread("minions_raw.jpg",0)
agera = cv2.imread("agrea.jpg",0)

#creating negative image
neg = 1 - img


##############################################################################
# log transformation on image, done on gray scale image
# formula :: opPix = ScalingConst * log(ipPix)
# ipPix - input pixel image
# opPix - output pixel image
# ScalingConst = 255/( log(max_input_pixel_value) )
# have to remove 0 from input matrix since, log(0) = inf

#removing 0 from the image
grayNonZero = np.where( gray==0 , 1, gray)

#modified formula since 0 has been removed from the array already
ScalingConst = 255 / np.log(np.max(grayNonZero))
logImg = ScalingConst * np.log(grayNonZero)

logImg = logImg.astype(np.uint8)

##############################################################################
#power log transformation/gamma transformation

gamma = 0.5
gammaImg= np.array( 255*(gray/255) ** gamma, dtype='uint8')

##############################################################################
#Piecewise - Linear Transformation Function -

def pixVal(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1/r1)*pix
    elif (r1 < pix and pix <= r2):
        return (s2 - s1)/(r2-r1) * (pix - r1) + s1
    else:
        return (255 - s1)/(255 - r1) * (pix - r2) + s2
    
r1, s1 = 100, 0
r2, s2 = 160, 180

pixVector = np.vectorize(pixVal)
contrastStretched = pixVector(agera, r1, s1, r2, s2)


cv2.imshow("original image", img)
cv2.imshow("agera image", agera)
cv2.imshow("negative image", neg)
cv2.imshow("gray scale image", gray)
cv2.imshow("log transformation image", logImg)
cv2.imshow("gamma transformation image - "+str(gamma), gammaImg)
cv2.imshow("piece wise linear transformation", contrastStretched)

cv2.imwrite("negativeImg.jpg", neg)
cv2.imwrite("log transformation.jpg", logImg)
cv2.imwrite("gamma transformation image - "+str(gamma)+".jpg", gammaImg)
cv2.imwrite("piece wise linear transformation.jpg", contrastStretched)

cv2.waitKey(0)
cv2.destroyAllWindows()