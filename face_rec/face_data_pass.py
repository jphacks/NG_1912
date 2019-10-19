# -*- coding: utf-8 -*-
import cv2
import os
import datetime
import time
from watson_developer_cloud import VisualRecognitionV3
from matplotlib import pyplot as plt
import json

visual_recognition = VisualRecognitionV3(
    #The release date of the version of the API you want to use.
    '2018-03-19',
    iam_apikey='ysXWcNeqrTKGhaTPiaz7zC6E-G7hXVYea_2IGMnCM9nf')

cap = cv2.VideoCapture(0)
HAAR_FILE = "C:/Users/sd16067/Documents/jpHacks/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)

def five_time_check():
    namelist=[]
    
    return namelist
def main():
    while True:
        namelist=[]
        #frame=cv2.imread("C:/Users/sd16067/Documents/jpHacks/data/syuugou01.jpg")
        ret, frame = cap.read(1)
        #img_g,_ = cv2.decolor(frame)
        #face = cascade.detectMultiScale(img_g)
        face = cascade.detectMultiScale(frame)
        if len(face)>0:
            print(face)
            j=0
            for x,y,w,h in face:
                face_cut = frame[y:y+h, x:x+w]
                cv2.imwrite('C:/Users/sd16067/Documents/jpHacks/data/faces/face_cut_{}.jpg'.format(j), face_cut)

                fname ='C:/Users/sd16067/Documents/jpHacks/data/faces/face_cut_{}.jpg'.format(j)
                with open(fname, 'rb') as images_file:
                    classes = visual_recognition.classify(
                    images_file,
                    threshold='0.6',
                    classifier_ids=["ZeseiCustomer_1325062844"]).get_result()
                    #unicodeで返ってくるので、utf-8に変換する。
                    result = json.dumps(classes, indent=2).encode('utf-8').decode('unicode_escape')
                    #jsonを辞書型にする
                    result = json.loads(result)
                    #認識結果のclass(=認識・特定した物体の名前)だけを抽出する。

                    print(result)
                    if len(result['images'][0]['classifiers'][0]['classes'])>0:
                        print("{}".format(result['images'][0]['classifiers'][0]['classes'][0]['class']))
                        namelist.append("{}".format(result['images'][0]['classifiers'][0]['classes'][0]['class']))
                    else:
                        print("unknown")
                        namelist.append("unknown")
                j+=1
        else:
            print('No face')
        j=0
        for x,y,w,h in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
            cv2.putText(frame,"{}".format(namelist[j]),(x+int(w/2),y),cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), lineType=cv2.LINE_AA)
            j+=1
        cv2.imwrite('C:/Users/sd16067/Documents/jpHacks/data/origin_image.jpg', frame)
        showimg=cv2.imread('C:/Users/sd16067/Documents/jpHacks/data/origin_image.jpg')
        b,g,r = cv2.split(showimg)
        img2 = cv2.merge([r,g,b])
        plt.imshow(img2)
        #plt.show()
        plt.draw()
        plt.pause(0.001)


if __name__ == '__main__':
    print("Start face recognition and date pass")
    main()
    print('end')
