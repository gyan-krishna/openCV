# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:26:17 2020
@author: Gyan Krishna

Example to demonstrate histogram analysis on a gray scale image
"""


import cv2
from matplotlib import pyplot as plt

img = cv2.imread("mario.jpg", 0)

hist_raw = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256],
                        ranges=[0, 256])
plt.show()

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
