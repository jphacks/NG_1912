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
import requests
import setting


visual_recognition = VisualRecognitionV3(
    #The release date of the version of the API you want to use.
    '2018-03-19',
    iam_apikey=setting.APIKEY)

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
HAAR_FILE = "C:/Users/sd16067/Documents/jpHacks/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)

def show_result0(frame,face,namelist):
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

def face_detect0(frame,face):
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
            classifier_ids=[setting.clICs]).get_result()
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
    show_result0(frame,face,namelist)
    return namelist

def show_result1(frame,face,namelist):
    if len(namelist)>0:
        i=0
        for x,y,w,h in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
            cv2.putText(frame,"{}".format(namelist[i]),(x+int(w/2),y),cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), lineType=cv2.LINE_AA)
            i+=1
    else:
        cv2.putText(frame,"No Face",(10,50),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), lineType=cv2.LINE_AA)
    #b,g,r = cv2.split(frame)
    #img2 = cv2.merge([r,g,b])
    #plt.imshow(img2)
    #plt.draw()
    #plt.pause(0.001)

def face_detect1(frame,face):
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
            classifier_ids=["zesei_customer_1164806800"]).get_result()#[setting.clICs]).get_result()
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
    show_result1(frame,face,namelist)
    return namelist

def five_time_check():
    namelist_eat=[]
    namelist_out=[]
    for i in range(5):
        _, frame0 = cap0.read(0)
        _, frame1 = cap1.read(1)
        face0 = cascade.detectMultiScale(frame0)
        face1 = cascade.detectMultiScale(frame1)
        if len(face0)>0:
            #print(face)
            appending_names=face_detect0(frame0,face0)
            namelist_eat[len(namelist_eat):len(appending_names)]=appending_names
        else:
            show_result0(frame0,face0,[])
            #print('No face')

        if len(face1)>0:
            #print(face)
            appending_names=face_detect1(frame1,face1)
            namelist_out[len(namelist_out):len(appending_names)]=appending_names
        else:
            show_result1(frame1,face1,[])
            #print('No face')
    namedic_eat={}
    namedic_out={}
    surched=[]
    for i in range(len(namelist_eat)):
        if namelist_eat[i] not in surched:
            surching=namelist_eat[i]
            namedic_eat["{}".format(surching)]=namelist_eat.count(surching)
            surched.append(surching)
    surched=[]
    for i in range(len(namelist_out)):
        if namelist_out[i] not in surched:
            surching=namelist_out[i]
            namedic_out["{}".format(surching)]=namelist_out.count(surching)
            surched.append(surching)
    #print(namedic)
    return namedic_eat,namedic_out

def send_namelist(namelist_eat,namelist_out):
    # TODO : here
    url_eat = "http://ec2-54-175-189-71.compute-1.amazonaws.com:8000/api/userEatIn/"
    url_out = "http://ec2-54-175-189-71.compute-1.amazonaws.com:8000/api/userStoreExit/"
    headers = {'Authorization' : 'Token f2845dc36277f7e63be82c1b9b00c09a4c8f3a16','content-type': "application/json"}
    for i in range(len(namelist_eat)):
        if namelist_eat[i] != 'unknown':
            payload = {'user_id' : namelist_eat[i]}
            requests.post(url_eat, data=json.dumps(payload), headers=headers)
    for i in range(len(namelist_out)):
        if namelist_out[i] != 'unknown':
            payload = {'user_id' : namelistout[i]}
            requests.post(url_out, data=json.dumps(payload), headers=headers)

    print("eat in space name {}".format(namelist_eat))
    print("out side name {}".format(namelist_out))

def main():
    while True:
        namelist_eat=[]
        namelist_out=[]
        namedic_eat,namedic_out=five_time_check()
        for key,value in namedic_eat.items():
            if value > 2:
                namelist_eat.append(key)
        for key,value in namedic_out.items():
            if value > 2:
                namelist_out.append(key)
        send_namelist(namelist_eat,namelist_out)


if __name__ == '__main__':
    print("Start face recognition and date pass")
    main()
    print('end')
