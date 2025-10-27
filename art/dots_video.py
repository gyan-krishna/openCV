import numpy as np
import cv2

rad = 4
spacing = 4
padding = 20
mat_dimm = (100, 80)

x_pix = (rad*2 + spacing)*mat_dimm[0] + padding
y_pix = (rad*2 + spacing)*mat_dimm[1] + padding

img_dimm = (y_pix, x_pix)
print(img_dimm)
img = np.zeros(img_dimm, dtype='uint8')
  
vid = cv2.VideoCapture(0)


while(True):
    ret, frame = vid.read()
    bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(bw,130,255,cv2.THRESH_BINARY)
    small = cv2.resize(thresh1, mat_dimm)
    
    img = np.zeros(img_dimm, dtype='uint8')
    for j in range(mat_dimm[0]):
        for i in range(mat_dimm[1]):
            x = padding+i*(rad*2+spacing)
            y = padding+j*(rad*2+spacing)
            
            if(small[i][j] == 255):
                cv2.circle( img, (y, x), rad, (255,255,255), -1)
    #img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('frame', frame)
    cv2.imshow('thresh', thresh1)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
vid.release()
cv2.destroyAllWindows()