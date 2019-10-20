import os
import random
import string
import base64
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from rest_framework import serializers
from app.users.models import User
from django.conf import settings
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import zipfile
import glob
from datetime import datetime
import shutil

class CustomLoginSerializer(LoginSerializer):
    email = serializers.EmailField()


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=150)
    images = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=False
    )

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'images': self.validated_data.get('images', '')
        }

    def ibm_learning(self, user_id, LEARNING_DATA_DIR_PATH):
        MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT')

        ZIP_PATH = os.path.join(MEDIA_ROOT,
                                ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.zip')
        with zipfile.ZipFile(ZIP_PATH, 'w') as z:
            for img_path in glob.glob(os.path.join(LEARNING_DATA_DIR_PATH, '*.jpg')):
                z.write(img_path, arcname=os.path.basename(img_path))

        IBM_IAMAUTHENTICATOR = getattr(settings, 'IBM_IAMAUTHENTICATOR')
        IBM_CLASSIFIER_ID = getattr(settings, 'IBM_CLASSIFIER_ID')

        authenticator = IAMAuthenticator(IBM_IAMAUTHENTICATOR)
        visual_recognition = VisualRecognitionV3(
            version='2018-03-19',
            authenticator=authenticator
        )
        with open(ZIP_PATH, 'rb') as dalmatian:
            classifiers = visual_recognition.update_classifier(
                classifier_id=IBM_CLASSIFIER_ID,
                positive_examples={user_id: dalmatian},
                negative_examples=None).get_result()

            ROOT_DIR = getattr(settings, 'ROOT_DIR')
            IBM_HISTORY_FILE_PATH = os.path.join(ROOT_DIR, "ibm_history.txt")
            with open(IBM_HISTORY_FILE_PATH, "a") as output_file:
                history = "[" + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "] " + str(classifiers)
                output_file.write(history)
                output_file.write(os.linesep)
            os.remove(ZIP_PATH)
            shutil.rmtree(LEARNING_DATA_DIR_PATH)

    def save(self, request):
        user = super(CustomRegisterSerializer, self).save(request)
        data = self.cleaned_data

        MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT')
        TARGET_IMG_DIR = os.path.join(MEDIA_ROOT,
                                      str(user.id))
        os.mkdir(TARGET_IMG_DIR)

        for encodeImage in data.get('images'):
            TARGET_IMG_PATH = os.path.join(TARGET_IMG_DIR,
                                           ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.jpg')
            _, encodeImage = encodeImage.split(",")

            with open(TARGET_IMG_PATH, 'bw') as f:
                f.write(base64.b64decode(encodeImage.encode()))

        self.ibm_learning(user.id, TARGET_IMG_DIR)
        return user


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
