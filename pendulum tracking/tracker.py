# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Mon Jan 18 23:01:36 2021
@author: Gyan Krishna

Topic: 
"""

import cv2
import numpy as np

vid = cv2.VideoCapture("pendulum01.mp4")
ret = True
while(vid.isOpened()):
    ret, frame = vid.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sat = np.array(hsv[:,:,1])
    ret, binary =  cv2.threshold(sat, 125, 255, cv2.THRESH_BINARY) 
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    final = cv2.bitwise_and(binary, gray, None)
    
    rows = final.shape[0]
    circles = cv2.HoughCircles(final, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=50, param2=15q,
                               minRadius=1, maxRadius=100)
    
    y, x = gray.shape
    
    mid = int(x/2)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            if(i.shape == (3,)):
                print(i)
                center = (i[0], i[1])
                # circle center
                cv2.circle(frame, center, 1, (0, 0, 255), 2)
                # circle outline
                radius = i[2]
                cv2.circle(frame, center, radius, (0, 255, 0), 2)
                frame = cv2.line(frame, (mid,0), center, (0,0,255), 2)
    
    
    
    cv2.imshow("video", final)
    cv2.imshow("video original", frame)
    if(cv2.waitKey(30) & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()
vid.release()
    

