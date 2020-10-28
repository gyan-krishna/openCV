# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:06:13 2020

@author: ASUS
"""

import cv2
import numpy as np


img = cv2.imread("agrea.jpg",0)
const = 0.5
# const < 1 if contrast supression,
# const > 1 if contrast enhancement

cv2.imshow("raw image",img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i][j] = np.uint8(img[i][j] * const)
        
cv2.imshow("contrasted image ("+str(const)+")",img)

cv2.imwrite("contrasted image ("+str(const)+").jpg",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
