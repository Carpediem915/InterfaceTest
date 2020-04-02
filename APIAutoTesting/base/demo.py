
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/2/20 14:46 
# @Author : hcm 
# @File : demo.py
# @desc :

import json
import requests

# get
# http://127.0.0.1:8000/getUser/?id=001
# post
# http://127.0.0.1:8000/login/

# url = 'http://127.0.0.1:8000/login/'
# data = {
#     'username': 'hcm',
#     'password': '1234'
# }

# url = 'http://127.0.0.1:8000/getuser/'
# data = {
#     'id': '001'
# }

# url = 'http://apis.juhe.cn/simpleWeather/query'
# data = {
#     'city': '成都',
#     'key': '060db39c6b279a6da8175572f0707572'
# }

class RunMain(object):
    """这是RunMain"""

    def __init__(self):
        pass

    def send_get(self, url, data):
            return requests.get(url=url, params = data).json()
        # json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False)

    def send_post(self, url, data):
        return requests.post(url=url, data=data).json()

    def run_main(self, url, method, data=None):
        # print('调用run_main方法')
        result = None
        if method == 'GET':
            result = self.send_get(url=url, data=data)
        else:
            result = self.send_post(url=url, data=data)
        return result

if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/getuser/'
    data = {
        'id': '001'
    }
    run = RunMain()
    res = run.run_main(url, 'GET', data)
    print(res)