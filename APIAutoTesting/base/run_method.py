#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/2/21 17:06 
# @Author : hcm 
# @File : run_method.py
# @desc :

import requests


class RunMethod(object):
    """这是RunMethod"""

    def __init__(self):

        pass

    def send_get(self, url, data, header=None):
        res = None
        # url = 'http://127.0.0.1:8000/getuser/'
        # data = {'id': '001'}
        if header != '':
            res = requests.get(url=url, params=data, headers=header)
        else:
            res = requests.get(url=url, params=data)
        return res

    def send_post(self, url, data, header=None):
        res = None
        if header != '':
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == "GET":
            res = self.send_get(url, data, header)
        else:
            res = self.send_post(url, data, header)
        return res.text
