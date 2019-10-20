# coding: UTF-8
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY= os.getenv("iam_apikey")
clICs=os.getenv("classifier_ids")
