from flask import Flask
from flask import request
from flask import make_response
from aip import AipFace
import base64
import json
from yuyin import soundAI
""" 你的 APPID AK SK """
APP_ID = '11262633'
API_KEY = 'vMCwrMzFb6AkgTqwac0IbXyg'
SECRET_KEY = '2vIr1XO9wviq0ma5KFKt0huC8fbhhwYo'
imageType = "BASE64"

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/renlianshibie',methods=['POST'])
def renlianshibie():
    print(request.form)
    
    res = client.faceverify([
        {
            'image': request.form['imgData'],
            'image_type': 'BASE64',
            'face_field':'age,beauty,expression,gender,glasses'
        }
        
    ])
    result = json.dumps(res)
    rst = make_response(result)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst,200

@app.route('/soundai')
def soundai():
    result  = soundAI.synthesis(request.args.get('content'), 'zh', 1, {
        'vol': 5,
    })
    print(result)
    if not isinstance(result, dict):
        with open('./static/audio/audio.mp3', 'wb') as f:
            f.write(result)
    rst = make_response('success')
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst,200
    
        


if __name__ == '__main__':
    app.run(port=7000,threaded=True)