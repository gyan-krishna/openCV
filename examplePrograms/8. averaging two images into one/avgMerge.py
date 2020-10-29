# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 22:11:29 2020

@author: Gyan Krishna
"""

import cv2
import numpy as np

rocket = cv2.imread("rocket.jpg")
nebula = cv2.imread("nebula.jpg")

rocketRes = cv2.resize(rocket, (nebula.shape[1], nebula.shape[0]))

x, y, channels = nebula.shape
merge = np.zeros(nebula.shape , dtype=np.uint8)

for i in range(x):
    for j in range(y):
        for k in range(channels):
            merge[i][j][k] = np.uint8( (rocketRes[i][j][k] + nebula[i][j][k])/2 )
            
print(rocketRes.shape)
print(nebula.shape)

cv2.imshow("nebula",nebula)
cv2.imshow("rocket",rocketRes)
cv2.imshow("merge",merge)


cv2.waitKey(0)
cv2.destroyAllWindows()
