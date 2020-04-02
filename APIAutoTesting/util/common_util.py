#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/2/25 17:34 
# @Author : hcm 
# @File : common_util.py
# @desc :


class CommonUtil(object):
    """这是CommonUtil"""

    def __init__(self):

        pass

    def is_contain(self, str_one, str_two):
        """
        判断一个字符串是否在另一个字符串中
        :param str_one: 查找的字符串
        :param str_two: 参考字符串
        :return:
        """
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag





