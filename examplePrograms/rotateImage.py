# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:40:54 2020
@author: Gyan Krishna

Example Program to rotate an image

"""


import cv2

img = cv2.imread("images\mario_raw.jpg")


##############################################################################
#                               METHOD 1                                     #
##############################################################################

cw1 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
ccw1 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
flip1 = cv2.rotate(img, cv2.ROTATE_180)

cv2.imshow("90 clockwise method 1", cw1)
cv2.imshow("90 counter clockwise method 1", ccw1)
cv2.imshow("180 rotate  method 1", flip1)

cv2.imwrite(r"images\rotate\90clockwiseMethod1.jpg", cw1)
cv2.imwrite(r"images\rotate\90counterClockwiseMethod1.jpg", ccw1)
cv2.imwrite(r"images\rotate\180rotateMethod1.jpg", flip1)


cv2.waitKey(0)
cv2.destroyAllWindows()
