# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 21:08:16 2020

@author: ASUS
"""
import cv2
import random
import numpy as np


def spNoise(img, prob):
    sp = np.copy(img)
    for i in range(sp.shape[0]):
        for j in range(sp.shape[1]):
            for k in range(sp.shape[2]):
                rnd = random.random()
                if(rnd < prob):
                    rnd = random.random()
                    if(rnd < 0.5):
                        sp[i][j] = 0
                    else:
                        sp[i][j] = 255
    return sp

img = cv2.imread("thanos.jpg")
saltAndPepper = spNoise(img, 0.0006)
gauss = cv2.GaussianBlur(img, (5,5), 10)

cv2.imshow("thanos original", img)
cv2.imshow("thanos salt and pepper", saltAndPepper)
cv2.imshow("thanos Gaussian noise", gauss)

cv2.imwrite("thanos salt and pepper.jpg", saltAndPepper)
cv2.imwrite("thanos Gaussian noise.jpg", gauss)


cv2.waitKey(0)
cv2.destroyAllWindows()

