# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Wed Nov  4 13:37:35 2020
@author: Gyan Krishna

Topic: 
"""

import dlib
import cv2

raw = cv2.imread("tony.jpg")
mask = cv2.imread("mask.png")
#mask2 = cv2.resize(mask, (raw.shape[1],raw.shape[0]))


det = dlib.get_frontal_face_detector()
pred = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

faces = det(raw)
for face in faces:
    x1 = face.left()
    y1 = face.top()      
    x2 = face.right()
    y2 = face.bottom()
    
    
    landmarks = pred(raw, face)
    yl1 = landmarks.part(28).y
    yl2 = landmarks.part(9).y
    dy = yl2 - yl1
    roi = raw[y1:y2, x1:x2]   
    mask2 = cv2.resize(mask, (roi.shape[1],dy))
    
    xlen = mask2.shape[0]
    ylen = mask2.shape[1]
    
    ydiff = yl1 - y1
    
    for i in range(xlen):
        for j in range(ylen):
            for k in range(3):
                if(mask2[i][j][k] != 0):
                    raw[i+y1+ydiff][j+x1][k] = mask2[i][j][k]

    cv2.imshow("raw",raw)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask2)
    
    cv2.imwrite("addedMask.jpg",raw)

cv2.waitKey(0)
cv2.destroyAllWindows()