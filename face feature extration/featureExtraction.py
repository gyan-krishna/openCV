import dlib
import cv2

cap = cv2.VideoCapture(0)

det = dlib.get_frontal_face_detector()
pred = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = det(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()

        x2 = face.right()
        y2 = face.bottom()

        landmarks = pred(gray, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y),2, (255, 0, 0), -1)

        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 3)

    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)
    if(key == 27):
        break

cap.release()
cv2.destroyAllWindows()