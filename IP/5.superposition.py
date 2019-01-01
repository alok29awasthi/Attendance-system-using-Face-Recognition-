import numpy as np
import cv2

img1=cv2.imread('graph1.png')
img2=cv2.imread('logo.png')

##add=img1+img2
#add=cv2.add(img1,img2)
##these add images pixel to pixel like [10,160,200]+[200,220,130]=[210,380,330]==[210,255,255]
weighted=cv2.addWeighted(img1,1,img2,0.5,0)

cv2.imshow('add',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
