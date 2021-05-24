# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sun May 23 16:17:59 2021
@author: Gyan Krishna

Topic:
"""

import cv2
import dlib
import numpy as np
import time

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

y, x, _ = frame.shape

detector = dlib.get_frontal_face_detector()

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()

        x2 = face.right()
        y2 = face.bottom()

        try:
            seconds = time.time()
            curr_time = time.ctime(seconds)

            cv2.putText(frame, str(curr_time), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA)

            face_crop = frame[y1:y2, x1:x2]
            blur_face = cv2.GaussianBlur(face_crop, (71,71), 0)
            frame[y1:y2, x1:x2] = blur_face
        except:
            print("error")

        #cv2.rectangle(frame, (x1,y1), (x2, y2), (0,0,255), 2)
        #cv2.imshow("face crop", blur_face)

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if(key == 27):
        break

cv2.destroyAllWindows()
cap.release()