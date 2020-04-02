#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/2/20 22:07 
# @Author : hcm 
# @File : mock_demo.py
# @desc :

import mock

# 模拟mock封装
def mock_test(mock_method, url, method, request_data, reponse_data):
    mock_method = mock.Mock(return_value=reponse_data)
    res = mock_method(url, method, request_data,)
    return res