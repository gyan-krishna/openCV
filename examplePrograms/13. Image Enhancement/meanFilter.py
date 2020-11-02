# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:09:47 2020

@author: Gyan Krishna
"""

import cv2
import numpy as np

img = cv2.imread("thanos salt and pepper.jpg")

meanFilter = cv2.blur(img, (3,3))
medianFilter = cv2.medianBlur(img,5)

kernel = np.ones((3,3), np.uint8) 
minFilter = cv2.erode(img, kernel)  
maxFilter = cv2.dilate(img, kernel)  


cv2.imshow("raw image", img)
cv2.imshow("mean Filter", meanFilter)
cv2.imshow("median Filter", medianFilter)
cv2.imshow("min Filter", minFilter) 
cv2.imshow("max Filter", maxFilter) 


cv2.imwrite("mean Filter.jpg", meanFilter)
cv2.imwrite("median Filter.jpg", medianFilter)
cv2.imwrite("min Filter.jpg", minFilter) 
cv2.imwrite("max Filter.jpg", maxFilter) 

cv2.waitKey(0)
cv2.destroyAllWindows()

