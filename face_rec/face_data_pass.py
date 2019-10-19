import cv2
import os
import datetime
import time
from watson_developer_cloud import VisualRecognitionV3
import json

visual_recognition = VisualRecognitionV3(
    #The release date of the version of the API you want to use.
    '2018-03-19',
    iam_apikey='CxC0kX07gkgV9Uqroaxz1b3b7BpRtAZnN1R1uN7DsHoE')

cap = cv2.VideoCapture(0)
HAAR_FILE = "./opencv/data/haarcascades/haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)
for i in range(5):
    print(i)
    ret, frame = cap.read(1)
    #img_g,_ = cv2.decolor(frame)
    #face = cascade.detectMultiScale(img_g)
    face = cascade.detectMultiScale(frame)
    if len(face)>0:
        print(face)
        j=0
        for x,y,w,h in face:
            face_cut = frame[y:y+h, x:x+w]
            cv2.imwrite('./data/faces/face_cut_{}.jpg'.format(j), face_cut)

            fname ='./data/faces/face_cut_{}.jpg'.format(j)
            with open(fname, 'rb') as images_file:
                classes = visual_recognition.classify(
                images_file,
                threshold='0.6',
                classifier_ids=["ZeseiCustomer_1427283252"]).get_result()
                #unicodeで返ってくるので、utf-8に変換する。
                result = json.dumps(classes, indent=2).encode('utf-8').decode('unicode_escape')
                #jsonを辞書型にする
                result = json.loads(result)
                #認識結果のclass(=認識・特定した物体の名前)だけを抽出する。
                print(result)
            j+=1
    else:
        print('No face')
    #白枠で顔を囲む
    for x,y,w,h in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
    cv2.imwrite('./data/origin_image_{}.jpg'.format(i), frame)
    #time.sleep(0.5)

print('end')
