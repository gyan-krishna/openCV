import numpy as np
import cv2

rad = 8
spacing = 8
padding = 20

mat_dimm = (40, 50)

x_pix = (rad*2 + spacing)*mat_dimm[0] + padding
y_pix = (rad*2 + spacing)*mat_dimm[1] + padding

img_dimm = (x_pix, y_pix)
print(img_dimm)
img = np.zeros(img_dimm, dtype='uint8')

for j in range(mat_dimm[0]):
    for i in range(mat_dimm[1]):
        x = padding+i*(rad*2+spacing)
        y = padding+j*(rad*2+spacing)
        
        cv2.circle( img, (x, y), rad, (255,255,255), -1)


cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()