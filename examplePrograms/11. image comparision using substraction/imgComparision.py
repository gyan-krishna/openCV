# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Mon Jan  4 19:47:56 2021
@author: Gyan Krishna

Topic: Image comparision by substraction.
"""

import cv2

img1 = cv2.imread("img1.png")
img2 = cv2.imread("img2.png")

sub = cv2.subtract(img2, img1);

cv2.imshow("image 1", img1)
cv2.imshow("image 2", img2)
cv2.imshow("comparision img", sub)
cv2.imwrite("result.png", sub)

cv2.waitKey(0)
cv2.destroyAllWindows()