import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _, frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red=np.array([110,50,50])
    upper_red=np.array([130,255,255])

    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)

##    cv2.imshow('res',res)
    
    kernel = np.ones((15,15),np.float32)/225
    blur = cv2.filter2D(res,-10,kernel)
    cv2.imshow('blur',blur)
    
    gaussian=cv2.GaussianBlur(res,(15,15),0)
    cv2.imshow('gaussian',gaussian)
    
    median=cv2.medianBlur(res,15)
    cv2.imshow('median',median)

    bilateral=cv2.bilateralFilter(res,15,75,75)
    cv2.imshow('bilateral',bilateral)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
