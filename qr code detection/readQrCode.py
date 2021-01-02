# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sat Jan  2 10:48:04 2021
@author: Gyan Krishna

Topic: 
"""

import cv2    #library to procress 
import pyzbar #library to procress bar/qr codes
#from pyzbar.pyzbar import decode

#qrcode.png
#barcode.jpg

img = cv2.imread("barcode.jpg")
codes = pyzbar.pyzbar.decode(img)

for code in codes:
    x1, y1, w, h = code.rect
    x2, y2 = w+x1, h+y1
    
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
    codeData = code.data.decode("utf-8")
    codeType = code.type
    print("found {} with data :: {}".format(codeType, codeData))

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
        