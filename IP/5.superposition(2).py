import numpy as np
import cv2

img1=cv2.imread('Picture1.png')
img2=cv2.imread('logo.png')

row,col,channel=img2.shape
roi=img1[0:row,0:col]

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_TOZERO)

mask_inv=cv2.bitwise_not(mask)

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask)

dst=cv2.add(img1_bg,img2_fg)
img1[0:row,0:col]=dst

cv2.imshow('mask',mask)
cv2.imshow('roi',roi)
cv2.imshow('bg',img1_bg)
cv2.imshow('fg',img2_fg)
cv2.imshow('img2gray',img2gray)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('dst',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
