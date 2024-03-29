# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sat Jan 23 10:26:37 2021
@author: Gyan Krishna

Topic:
"""

import cv2

img = cv2.imread("rocket.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)         #reduction of noise

ksize = 3               #kernel size
ddepth = cv2.CV_16S     #desired depth
lap = cv2.Laplacian(blur, ddepth, ksize)
lap = cv2.convertScaleAbs(lap)

cv2.imshow("rocket racoon grayscale",gray)
cv2.imshow("rocket racoon laplacian",lap)

cv2.imwrite("laplacian.jpg",lap)

cv2.waitKey(0)
cv2.destroyAllWindows()