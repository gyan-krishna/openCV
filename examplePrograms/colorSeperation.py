# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:40:13 2020
@author: Gyan Krishna

performing color seperation into blue green and red channels from bgr image

"""


import cv2

img = cv2.imread("mario.jpg")

blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]

cv2.imshow("original image", img)
cv2.imshow("blue channel", blue)
cv2.imshow("green channel", green)
cv2.imshow("red channel", red)

cv2.waitKey(0)
cv2.destroyAllWindows()
