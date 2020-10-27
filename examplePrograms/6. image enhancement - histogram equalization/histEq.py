# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:46:01 2020

@author: ASUS
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("mario_raw.jpg", 0)
eq = cv2.equalizeHist(img)

cv2.imshow("raw image",img)
cv2.imshow("equalised image", eq)

hist_raw = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256],
                        ranges=[0, 256])
hist_eq = cv2.calcHist(images=[eq], channels=[0], mask=None, histSize=[256],
                        ranges=[0, 256])

fig, plots = plt.subplots(2)
fig.tight_layout(pad=3.0)


plots[0].plot(hist_raw)
plots[0].set_title('raw image hist')

plots[1].plot(hist_eq)
plots[1].set_title('equilised image hist')
plt.plot()


cv2.waitKey(0)
cv2.destroyAllWindows()


