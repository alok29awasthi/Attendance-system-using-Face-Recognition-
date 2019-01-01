import numpy as np
import cv2

img=cv2.imread('wrist_watch.jpg',cv2.IMREAD_COLOR)
px=img[55,55]

img[100:150, 100:150]=[102,119,200]
watch=img[150:250,200:300]
img[0:100,100:200]=watch

print(px)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
