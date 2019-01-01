import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    rev,frame=cap.read()
    hls=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.flip(frame,1)
    cv2.imshow('frame',frame)
    cv2.imshow('hls',hls)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
