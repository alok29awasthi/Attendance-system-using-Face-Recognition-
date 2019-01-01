import cv2
import os
import time

name=input('Enter your name: ')
name='\\'+name
newpath =r'C:\Users\Alok Awasthi\Desktop\Project\Face recognition\images'+name

##print(newpath)
if not os.path.exists(newpath):
    os.makedirs(newpath)
else:
    print("Directory already exists")
    exit()
path = r'C:\Users\Alok Awasthi\Desktop\Project\Face recognition\images'+name

face_cascade=cv2.CascadeClassifier('cascade/haarcascade_frontalface_alt2.xml')

cap=cv2.VideoCapture(0)
i=1

while(True):
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)

    i=str(i)
    pic=i+'.png'
    
    for(x,y,w,h) in faces:
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x+w]
        color=(255,255,255)
        stroke=2
        img=gray
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
##        cv2.imwrite(pic,img)
        cv2.imwrite(os.path.join(path , pic), img)
        print(i)
        i=int(i)
        i=i+1
        time.sleep(0.5)
    
    if(i==21):
        break
            
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff==27:
        break

cap.release()
cv2.destroyAllWindows()
