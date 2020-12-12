import numpy as np
import cv2
import pickle
import sqlite3

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read("trainner.yml")
# labels= {}
# with open("labels.pickle", 'rb') as f:
#     labels = pickle.load(f)

def insertOrUpdate(Id,Name):
    conn=sqlite3.connect("FaceBase.db")
    c = conn.cursor()
    # print("heyyy")
    cmd="SELECT * FROM TC1_7 WHERE ID="+str(Id)
    cursor=c.execute(cmd)
    # print(cursor)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if isRecordExist==1:
        cmd="UPDATE TC1_7 SET Name=? WHERE ID=?"
        params = (str(Name),str(Id))
    else:
        cmd = "INSERT INTO TC1_7(ID,Name) VALUES(?,?)"
        params = (str(Id),str(Name))
    c.execute(cmd,params)
    conn.commit()
    conn.close()

cap = cv2.VideoCapture(0)
id = input('enter user id: ')
name = input('Enter username: ')
insertOrUpdate(id,name)
sampleNum = 0
while(True):

    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]

        # id_, conf = recognizer.predict(roi_gray)
        # if conf>=45 and conf<=85:
        #     print(id_)
        # else:
        #  =    print('n')

        # img_item = "my-img.png"
        # cv2.imwrite(img_item, roi_gray)
        sampleNum = sampleNum + 1
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",roi_gray)
        color = (255,0,0)
        stroke = 2
        width = x + w
        height = y + h
        cv2.rectangle(frame, (x,y), (width,height), color, stroke)
        cv2.waitKey(100)
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
    if(sampleNum>20):
        break
    # if cv2.waitKey(20) & 0xFF == ord('q'):
    #     break

cap.release()
cv2.destroyAllWindows()

#Output: C:/Users/Administrator/AppData/Local/Programs/Python/Python38/python.exe E:/hiral/Python/Python_project/dataset_creator.py
#Python version: Python 3.8.5 64-bit
#pip install virtualenvwrapper-win
#mkvirtualenv test1
# python manage.py runserver