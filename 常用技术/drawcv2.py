import numpy as np 
import cv2
import json

from aip import AipFace
import base64

""" 你的 APPID AK SK """
APP_ID = '11262633'
API_KEY = 'vMCwrMzFb6AkgTqwac0IbXyg'
SECRET_KEY = '2vIr1XO9wviq0ma5KFKt0huC8fbhhwYo'
imageType = "BASE64"

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
jpg1 = base64.b64encode(open('./3.jpg', 'rb').read())
jpg1 = bytes.decode(jpg1)
res = client.faceverify([
    {
        'image': jpg1,
        'image_type': 'BASE64',
        'face_field':'age,beauty,expression,gender,glasses'
    }
    
])
print(res)
# res =  json.loads(result)

jpg1 =  cv2.imread('./3.jpg')
for item in res['result']['face_list']:
    x1 = int(item['location']['left'])
    y1 = int(item['location']['top'])
    x2 = int(item['location']['left']+item['location']['width'])
    y2 = int(item['location']['top']+item['location']['height'])
    cv2.rectangle(jpg1, (x1,y1), (x2,y2), (0, 255, 0), 2)





cv2.imshow('capture',jpg1)
cv2.waitKey(0)