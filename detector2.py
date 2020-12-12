import numpy as np
import cv2
import pickle
import sqlite3

detectedFaces = []
    # face_cascade = cv2.CascadeClassifier('C:/Users/Administrator/projects/AttendanceProject/login/cascades/data/haarcascade_frontalface_alt2.xml')
face_cascade = cv2.CascadeClassifier('C:/Users/Administrator/projects/AttendanceProject/login/cascades/data/haarcascade_frontalface_default.xml')
    # cap = cv2.VideoCapture(0)
def getProfile(id):
    con = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM TC1_7 WHERE ID="+str(id)
    cursor = con.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    con.close()
    return profile

cap=cv2.imread("C:/Users/Administrator/projects/AttendanceProject/login/detection/20180325_230342.jpg")
cap=cv2.resize(cap, (960, 960))
    # rec = cv2.face.LBPHFaceRecognizer_create()
rec = cv2.face.LBPHFaceRecognizer_create(1,8,8,8,100)
rec.read("recognizer\\tranningData.yml")
id=0
font = cv2.FONT_HERSHEY_SIMPLEX
while(True):
        # ret,frame = cap.read()
    frame = cap
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x + w,y + h), (0,0,255), 2)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        print(id)
        profile = getProfile(id)
        if(profile!=None):
            cv2.putText(frame, str(profile[0]),(x,y+h), font,2,(255,255,255),2,cv2.LINE_AA)
            cv2.putText(frame, str(profile[1]),(x,y+h+30), font,2,(255,255,255),2,cv2.LINE_AA)
            print(str(profile[0])+' '+str(profile[1]))
    cv2.imshow('frame',frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cap.release()
cv2.destroyAllWindows()