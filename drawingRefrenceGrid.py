"""
Python code to draw reference grid lines on an image
@author: Gyan Krishna Sreekar
"""
import cv2


def draw_grid(img):
    color = (0, 0, 255)
    font = cv2.FONT_HERSHEY_PLAIN
    if len(img.shape) == 3:
        y, x, _ = img.shape
    else:
        y, x = img.shape
    print(x, y)
    for i in range(0, x, 100):
        img = cv2.line(img, (i, 20), (i, y), color, 2)
        img = cv2.putText(img, str(i), (i, 15), font, 1, color, 1, cv2.LINE_AA)
    for i in range(0, y, 100):
        img = cv2.line(img, (40, i), (x, i), color, 2)
        img = cv2.putText(img, str(i), (5, i), font, 1, color, 1, cv2.LINE_AA)
    return img


if __name__ == "__main__":
    image = cv2.imread("ironman.jpg")
    edit = draw_grid(image)
    cv2.imshow("edit", edit)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
