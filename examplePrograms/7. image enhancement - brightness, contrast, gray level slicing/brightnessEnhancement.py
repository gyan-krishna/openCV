# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:08:43 2020

@author: Gyan Krishna
"""

import cv2

img = cv2.imread("agrea.jpg",0)
const = 50

cv2.imshow("raw image",img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if(img[i][j] + const > 255):
            img[i][j] = 255
        else:
            img[i][j] += const


cv2.imshow("enhancement image",img)
cv2.imwrite("brightness enhancement image.jpg",img)

cv2.waitKey(0)
cv2.destroyAllWindows()