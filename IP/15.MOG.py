import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame=cap.read()
    fgmask=fgbg.apply(frame)

    cv2.imshow('original',frame)
    cv2.imshow('fg',fgmask)

    if (cv2.waitKey(1) & 0xff==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
