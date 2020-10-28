# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:08:43 2020

@author: ASUS
"""

import cv2

img = cv2.imread("agrea.jpg",0)
const = 50
#enh = img + 50

cv2.imshow("raw image",img)
cv2.imshow("enhancement image",enh)

cv2.waitKey(0)
cv2.destroyAllWindows()