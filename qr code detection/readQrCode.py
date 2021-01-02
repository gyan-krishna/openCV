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


sampleFiles = ["qrcode.jpg", "barcode.jpg"]
sampleOPFiles = ["qrcodeOP.png", "barcodeOP.jpg"]
fileNo = 1

img = cv2.imread(sampleFiles[fileNo])
codes = pyzbar.pyzbar.decode(img)

for code in codes:
    x1, y1, w, h = code.rect
    x2, y2 = w+x1, h+y1
    
    codeData = code.data.decode("utf-8")
    codeType = code.type
    
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
    img = cv2.putText(img, codeType, (x1+20, y1+40), cv2.FONT_HERSHEY_SIMPLEX , 1, (0,0,255), 2, cv2.LINE_AA)
    img = cv2.putText(img, codeData, (x1+20, y1+100), cv2.FONT_HERSHEY_SIMPLEX , 1, (0,0,255), 2, cv2.LINE_AA)
    print("found {} with data :: {}".format(codeType, codeData))

cv2.imshow("image",img)
cv2.imwrite(sampleOPFiles[fileNo], img)
cv2.waitKey(0)
cv2.destroyAllWindows()
        