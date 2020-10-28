# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:57:38 2020

@author: Gyan Krishna
"""

import cv2

img = cv2.imread("agrea.jpg",0)
const = 50

cv2.imshow("raw image",img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if(img[i][j] - const < 0):
            img[i][j] = 0
        else:
            img[i][j] -= const

cv2.imshow("enhancement image",img)
cv2.imwrite("brightness supression image.jpg",img)

cv2.waitKey(0)
cv2.destroyAllWindows()