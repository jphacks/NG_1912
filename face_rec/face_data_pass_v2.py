# -*- coding: utf-8 -*-
import cv2
import os
import datetime
import time
from watson_developer_cloud import VisualRecognitionV3
from matplotlib import pyplot as plt
from dotenv import load_dotenv
import json
import collections
import setting

visual_recognition = VisualRecognitionV3(
    #The release date of the version of the API you want to use.
    '2018-03-19',
    iam_apikey=setting.APIKEY)

cap = cv2.VideoCapture(0)
HAAR_FILE = "C:/Users/sd16067/Documents/jpHacks/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)

def show_result(frame,face,namelist):
    if len(namelist)>0:
        i=0
        for x,y,w,h in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
            cv2.putText(frame,"{}".format(namelist[i]),(x+int(w/2),y),cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), lineType=cv2.LINE_AA)
            i+=1
    else:
        cv2.putText(frame,"No Face",(10,50),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), lineType=cv2.LINE_AA)
    b,g,r = cv2.split(frame)
    img2 = cv2.merge([r,g,b])
    plt.imshow(img2)
    plt.draw()
    plt.pause(0.001)

def face_detect(frame,face):
    i=0
    namelist=[]
    appended_names=[]
    for x,y,w,h in face:
        face_cut = frame[y:y+h, x:x+w]
        cv2.imwrite('C:/Users/sd16067/Documents/jpHacks/data/faces/face_cut_{}.jpg'.format(i), face_cut)

        fname ='C:/Users/sd16067/Documents/jpHacks/data/faces/face_cut_{}.jpg'.format(i)
        with open(fname, 'rb') as images_file:
            classes = visual_recognition.classify(
            images_file,
            threshold='0.6',
            classifier_ids=setting.clICs).get_result()
            #unicodeで返ってくるので、utf-8に変換する。
            result = json.dumps(classes, indent=2).encode('utf-8').decode('unicode_escape')
            #jsonを辞書型にする
            result = json.loads(result)

            if len(result['images'][0]['classifiers'][0]['classes'])>0:
                #print("{}".format(result['images'][0]['classifiers'][0]['classes'][0]['class']))
                appending_name="{}".format(result['images'][0]['classifiers'][0]['classes'][0]['class'])
                if appending_name not in appended_names:
                    namelist.append(appending_name)
                    appended_names.append(appended_names)
            else:
                #print("unknown")
                namelist.append("unknown")
        i+=1
    show_result(frame,face,namelist)
    return namelist

def five_time_check():
    namelist=[]
    for i in range(5):
        ret, frame = cap.read(0)
        face = cascade.detectMultiScale(frame)
        if len(face)>0:
            #print(face)
            appending_names=face_detect(frame,face)
            namelist[len(namelist):len(appending_names)]=appending_names
        else:
            show_result(frame,face,[])
            #print('No face')
    namedic={}
    surched=[]
    for i in range(len(namelist)):
        if namelist[i] not in surched:
            surching=namelist[i]
            namedic["{}".format(surching)]=namelist.count(surching)
            surched.append(surching)
    print(namedic)
    return namedic

def send_namelist(namelist):
    # TODO : here
    print(namelist)

def main():
    while True:
        namelist=[]
        namedic=five_time_check()
        for key,value in namedic.items():
            if value > 2:
                namelist.append(key)
        send_namelist(namelist)


if __name__ == '__main__':
    print("Start face recognition and date pass")
    main()
    print('end')
