import cv2
import numpy as np

c=0
img=cv2.imread('corner.jpg')
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

corners=cv2.goodFeaturesToTrack(gray, 60, 0.01, 10)
corners=np.int0(corners)

for corner in corners:
    x, y=corner.ravel()
    cv2.circle(img, (x,y), 5, 100, -5)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
