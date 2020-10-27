#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
pip install baidu-aip
"""
import base64
from aip import AipFace
# 配置百度aip参数
APP_ID = '15768642'
API_KEY = 'xhiiGmGPRCRj10XIqVlVeCky'
SECRET_KEY = 'ZDMMAO7StwTKzW8BspVQxvoGtdgSW4yI'
a_face = AipFace(APP_ID, API_KEY, SECRET_KEY)
image_type = 'BASE64'
options = {'face_field': 'age,gender,beauty'}
def get_file_content(file_path):
  """获取文件内容"""
  with open(file_path, 'rb') as fr:
    content = base64.b64encode(fr.read())
    return content.decode('utf8')
def face_score(file_path):
  """脸部识别分数"""
  result = a_face.detect(get_file_content(file_path), image_type, options)
  print(result)
  age = result['result']['face_list'][0]['age']
  beauty = result['result']['face_list'][0]['beauty']
  gender = result['result']['face_list'][0]['gender']['type']
  return age, beauty, gender
class ScoreSystem():
    # 获取百度API接口获得的年龄、分数、性别
    age, score, gender = face_score("./1.jpg")
    print("性别：" + str(gender))
    print("年龄：" + str(age))
    print("颜值：" + str(score))
