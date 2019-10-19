from watson_developer_cloud import VisualRecognitionV3
import json

class Watson:
    def __init__(self):
        self.visual_recognition = VisualRecognitionV3(
            #The release date of the version of the API you want to use.
            '2018-03-19',
            iam_apikey='ysXWcNeqrTKGhaTPiaz7zC6E-G7hXVYea_2IGMnCM9nf')

        self.cap = cv2.VideoCapture(0)
        self.HAAR_FILE = "C:/Users/sd16067/Documents/jpHacks/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
        self.cascade = cv2.CascadeClassifier(self.HAAR_FILE)
        self.face=[]
        self.fname=""

    def get_face_image(self):
        ret, frame = self.cap.read(1)
        self.face = self.cascade.detectMultiScale(frame)

    def Open_Result(self,fname):
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
                    print("{}".format(result['images'][0]['classifiers'][0]['classes'][0]['class']))
                j+=1
        else:
            print('No face')
