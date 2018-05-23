from aip import AipSpeech
import os
""" 你的 APPID AK SK """
APP_ID = '11281953'
API_KEY = 'DXrAftkcRz82MNIMXC7zltuX'
SECRET_KEY = 'nefvKfjv85wD5lz7Evlr6Zf4O9YN4VYS'

soundAI = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# result  = client.synthesis('陈子月宝宝真乖，不哭哈', 'zh', 1, {
#     'vol': 5,
# })

# # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
# if not isinstance(result, dict):
#     with open('auido.mp3', 'wb') as f:
#         f.write(result)
#     os.system('auido.mp3')
