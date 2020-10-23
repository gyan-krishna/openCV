# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:12:26 2020
@author: Gyan Krishna

Example program for conversion of image formats
1. BGR      to  Gray
2. gray     to  binary
3. BGR      to  HSV
4. HSV      to  BGR
5. BGR      to  YCbCr
6. YCbCr    to  BGR

BGR     - Red Green Blue
HSV     - Hue Saturation Value
YCbCr   - Green (Y), Blue (Cb), Red (Cr)
"""


import cv2

img = cv2.imread("images\mario_raw.jpg")

# conversion from RGB to Gray Scale
grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# conversion from Gray Scale to Binary
_, binary1 = cv2.threshold(grayScale, 255/2, 255, cv2.THRESH_BINARY)

# conversion from RGB to binary


# conversion of rgb to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# conversion of HSV to RGB
rgb_from_hsv = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)

# conversion of RGB to YCbCr
YCbCr = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

# conversion of YCbCr to RGB
rgb_from_ycbcr = cv2.cvtColor(img, cv2.COLOR_YCR_CB2RGB)


cv2.imshow("original imaage     ", img)
cv2.imshow("gray scale imaage   ", grayScale)
cv2.imshow("binary image        ", binary1)
cv2.imshow("HSV image           ", hsv)
cv2.imshow("BGR from HSV image  ", rgb_from_hsv)
cv2.imshow("YCbCr image         ", YCbCr)
cv2.imshow("bgr from YCbCr image", rgb_from_ycbcr)

cv2.imwrite(r"images\formatConversion\original imaage.jpg", img)
cv2.imwrite(r"images\formatConversion\gray scale imaage.jpg", grayScale)
cv2.imwrite(r"images\formatConversion\binary image.jpg", binary1)
cv2.imwrite(r"images\formatConversion\HSV image.jpg", hsv)
cv2.imwrite(r"images\formatConversion\BGR from HSV image.jpg", rgb_from_hsv)
cv2.imwrite(r"images\formatConversion\YCbCr image.jpg", YCbCr)
cv2.imwrite(r"images\formatConversion\bgr from YCbCr image.jpg", rgb_from_ycbcr)

cv2.waitKey(0)
cv2.destroyAllWindows()
