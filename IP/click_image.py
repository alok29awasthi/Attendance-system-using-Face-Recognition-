import cv2
import numpy as np

cap = cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier('cascade/haarcascade_frontalface_alt2.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    cv2.imshow('frame',frame)
    for(x,y,w,h) in faces:
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x+w]
    cv2.imwrite('image1.jpg',roi_color);

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
