import numpy as np
import cv2
import pickle
import operator
from operator import itemgetter

face_cascade=cv2.CascadeClassifier('cascade/haarcascade_frontalface_alt2.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

temp = {}
students=['aunny','alia','bunny']
countnames = {'aunny':0,'alia':0,'bunny':0}
names=[]
i=0
j=0

labels={"person_name": 1}
with open("labels.pickle",'rb') as f:
    og_labels=pickle.load(f)
    labels={v:k for k,v in og_labels.items()}

cap=cv2.VideoCapture(0)
i=0
face={}

while(True):
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    
    for(x,y,w,h) in faces:
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x+w]

        id_, conf=recognizer.predict(roi_gray)
        if conf>=45 and conf<=85:
##            print(id_, conf)
##            print(labels[id_])
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=labels[id_]
            print(id_)
            color=(255,255,255)
            stroke=2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            
            names=names + [name]
            if name in students:
                countnames[name]+=1
##                print(countnames[name])
                if(countnames[name]==20):
                    face[name]='Present'
                    print(face)
                    countnames[name]+=1
                    students.remove(name)

                    i=0   
                    while i<3:
                        countnames[list(countnames.keys())[i]]=0
                        i=i+1
                    print(countnames)

##                  print(list(countnames.keys())[0])
##                  print(students)
                    
            
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff==27:
        break

cap.release()
cv2.destroyAllWindows()

for faces in students:
    if faces not in face:
        face[faces]='Absent'
        
print(face)
