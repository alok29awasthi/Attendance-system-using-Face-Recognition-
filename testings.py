import operator
from operator import itemgetter
import os
#Firstly we make the folder path.
path=r'C:\Users\Alok Awasthi\Desktop\Project\Face recognition\images\sunny'
##os.makedirs(path)
#then we change the directory that python looks at to the new place

##i=int(input('enter'))
##i=str(i)
##pic=i+'.png'
##i=int(i)
##print(pic)
##i=i+1
##print(i)

names=[]
stud={}
i=0
f=['c','b','a','e','d','a','a','d']
names=['aunny','alia','bunny']
face={'alia':'Present','bunny':'Present'}
for faces in names:
    if faces not in face:
        face[faces]='Absent'
print(face)
countnames = {'aunny':0,'alia':2,'bunny':0}
countnames[names[2]]=0+1
items=list(countnames.keys())
print(len(items))
print('dictionary\n',list(countnames.keys()))
sorted(countnames.values())
sort=sorted(countnames.items(), key=itemgetter(1))
sort.reverse()
##print(sort)
face={}
print(list(sort)[0][0])
face[list(sort)[0][0]]='Present'
face['aunny']='Present'
print(face)
name='aunny'
i=0
countnames[name]+=5
print(countnames)
##print(countnames)
##print(list(countnames.values())[0]+5)
print(list(countnames.keys())[0])
##while i<5:
##    text = input()
##    names = names + [text]
##    i=i+1
##    temp = {}
##    for name in names:
##        name = name.lower()
##        if name in temp:
##            temp[name] += 1
##        else:
##            temp[name] = 1
##    countnames = {}
##    for key, value in temp.items():
##        if value in countnames:
##            countnames[value].append(key)
##        else:
##            countnames[value] = [key]
##n=countnames[list(countnames.keys())[0]]
##faces[n[0]]='Present'
##print(n[0])
##names.remove(n[0])
##print(names)
##print(f)
##if(f):
##    for face in f:
##        faces[face]='Absent'
##print(faces)
##
##for key in sorted(faces):
##    print("%s: %s" % (key, faces[key]))
