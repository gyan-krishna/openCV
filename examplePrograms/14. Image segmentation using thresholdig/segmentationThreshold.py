# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Mon Jan  4 21:49:40 2021
@author: Gyan Krishna

Topic: 
"""

import cv2

xray = cv2.imread("hand_xray.jpeg",0)
x, y, = xray.shape

x, y = int(x/3), int(y/3)

xray = cv2.resize(xray, (y,x))
ret, thresh = cv2.threshold(xray, 115, 255, cv2.THRESH_BINARY)


cv2.imshow("raw", xray)
cv2.imshow("thresh", thresh)

cv2.imwrite("segmented.jpg",thresh)
cv2.waitKey(0);
cv2.destroyAllWindows()