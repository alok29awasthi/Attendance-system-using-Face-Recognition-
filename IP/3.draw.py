import cv2
import numpy as np

txt=input('Enter text: ')

img = cv2.imread('wrist_watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255,255,100), 15)

cv2.rectangle(img, (0,0), (150,150), (100,100,100), -5)

cv2.circle(img, (75,75), 75, (0,255,100), -100)
#cv2.circle(img, (CENTER,CENTER), radius, color, width)

pts=np.array([[5,5],[30,30],[60,5],[75,78],[110,40],[310,89],[65,288]], np.int32)
cv2.polylines(img,[pts],True,(0,0,0),1,4,0)
#cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])

font=cv2.FONT_HERSHEY_PLAIN
#FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, FONT_HERSHEY_DUPLEX, FONT_HERSHEY_COMPLEX, FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL, FONT_HERSHEY_SCRIPT_SIMPLEX, or FONT_HERSHEY_SCRIPT_COMPLEX,

cv2.putText(img,txt,(400,600),font,1,(255,255,255),3,cv2.LINE_AA)
#cv2.putText(img,'Sample text',(X,Y),font,size(can be floating value),color,thickness,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
