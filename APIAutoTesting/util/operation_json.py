#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/2/21 11:02 
# @Author : hcm 
# @File : operation_json.py
# @desc :

import json
from public import config

# fp = open('../config/login.json')
# data = json.load(fp)
# print(data['login'])


class OperationJson(object):
    """这是OperationJson"""

    def __init__(self):
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        filneame = config.src_path + "/config/login.json"
        with open(filneame) as f:
            data = json.load(f)
            return data

    def get_data(self, id):
        return self.data[id]

if __name__ == '__main__':
    opjson = OperationJson()
    data = opjson.get_data('login')
    print(data)