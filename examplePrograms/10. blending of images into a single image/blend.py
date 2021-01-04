# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Mon Jan  4 21:20:09 2021
@author: Gyan Krishna

Topic: blending of images into a single image
"""

import cv2

mickey = cv2.imread("mickey.jpg")
background = cv2.imread("background.jpg")

print(mickey.shape)
print(background.shape)

x, y, _ = mickey.shape
background = cv2.resize(background, (y,x) )

merge = cv2.addWeighted(mickey, 0.6, background, 0.4, 0)

cv2.imshow("mickey",mickey)
cv2.imshow("background", background)
cv2.imshow("merge", merge)


cv2.waitKey(0);
cv2.destroyAllWindows()