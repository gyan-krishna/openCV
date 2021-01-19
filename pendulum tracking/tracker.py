# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Mon Jan 18 23:01:36 2021
@author: Gyan Krishna

Topic: 
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

vid = cv2.VideoCapture("pendulum01.mp4")
ret = True

x_pts = []
y_pts = []
npts = 0
while(vid.isOpened()):
    
    ret, frame = vid.read()
    if(ret == None):
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sat = np.array(hsv[:,:,1])
    ret, binary =  cv2.threshold(sat, 125, 255, cv2.THRESH_BINARY) 
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    final = cv2.bitwise_and(binary, gray, None)
    
    rows = final.shape[0]
    circles = cv2.HoughCircles(final, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=50, param2=15,
                               minRadius=1, maxRadius=100)
    
    y, x = gray.shape
    mid = int(x/2)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            if(i.shape == (3,)):
                #print(i)
                radius = i[2]
                center = (i[0], i[1])
                
                pt = int(center[1])
                x_pts.append(pt)
                y_pts.append(npts)
                
                npts = npts+1
                cv2.circle(frame, center, 1, (0, 0, 255), 2)
                cv2.circle(frame, center, radius, (0, 255, 0), 2)
                frame = cv2.line(frame, (mid,0), center, (0,0,255), 2)
                
    cv2.imshow("video", final)
    cv2.imshow("video original", frame)
    if(cv2.waitKey(30) & 0xFF == ord('q')):
        break

plt.plot(y_pts,x_pts)
plt.show()

cv2.destroyAllWindows()
vid.release()
    

