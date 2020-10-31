# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 23:58:41 2020

@author: Gyan Krishna
"""

import cv2
import numpy as np

rocket = cv2.imread("rocket.jpg")
nebula = cv2.imread("nebula.jpg")

img1 = cv2.imread("Snapshot_1.png")
img2 = cv2.imread("Snapshot_2.png")

x, y, _ = img1.shape

x = int(x/2)
y = int(y/2)

img1 = cv2.resize(img1, (y,x))
img2 = cv2.resize(img2, (y,x))

rocketRes = cv2.resize(rocket, (nebula.shape[1], nebula.shape[0]))

sum = cv2.add(rocketRes, nebula)
weightedSum = cv2.addWeighted(rocketRes,0.8,nebula,0.3,0)
diff = cv2.subtract(img2, img1)

cv2.imshow("weighted sum",weightedSum)
cv2.imshow("sum",sum)
cv2.imshow("img 1",img1)
cv2.imshow("img 2",img2)

cv2.imshow("diff",diff)

cv2.imwrite("weightedSum.jpg",weightedSum)
cv2.imwrite("NonWeightedSum.jpg",sum)
cv2.imwrite("weightedSum.jpg",sum)

cv2.waitKey(0)
cv2.destroyAllWindows()