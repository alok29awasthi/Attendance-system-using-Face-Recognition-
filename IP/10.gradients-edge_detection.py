import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    rev,frame = cap.read()
    frame=cv2.flip(frame,1)
    laplacian=cv2.Laplacian(frame, cv2.CV_16S)
    sobelx=cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely=cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges=cv2.Canny(frame,100,50)
##    cv2.imshow('original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('edges',edges)
    

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
