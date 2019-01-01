import numpy as np
import os
from PIL import Image
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR,"images")

face_cascade=cv2.CascadeClassifier('cascade/haarcascade_frontalface_alt2.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()
##recognizer= cv2.face.FisherFaceRecognizer_create()
##cv2.face.createLBPFaceRecognizer()
##recognizer= cv2.face.FisherFaceRecognizer_create()
current_id = 0
label_ids = {}
x_train = []
y_labels = []

for root, dirs, files in os.walk(image_dir):
        for file in files:
                if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
                        path = os.path.join(root, file)
                        label = os.path.basename(root).replace(" ","-").lower()
                        if label in label_ids:
                                pass
                        else:
                                label_ids[label] = current_id
                                current_id += 1

                        id_ = label_ids[label]
##                        print(label_ids)
##                        print(label)
##                        y_labels.append(label)
##                        x_train.append(path)
                        pil_image =Image.open(path).convert("L")
                        
                        i=1
##                        print(pil_image,i)
                        i+=1
                        size=(550,550)
##                        final_image=pil_image.resize(size, Image.ANTIALIAS)
                        image_array = np.array(pil_image, "uint8")
                        image_array=cv2.GaussianBlur(image_array,(5,5),0)
##                        print(image_array)
                        faces=face_cascade.detectMultiScale(image_array,1.3,5)
                        
                        for (x,y,w,h) in faces:
                                roi=image_array[y:y+h, x:x+w]
                                x_train.append(roi)
                                y_labels.append(id_)


with open("labels.pickle",'wb') as f:
        pickle.dump(label_ids,f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")


