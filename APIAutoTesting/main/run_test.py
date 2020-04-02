#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/2/22 10:50 
# @Author : hcm 
# @File : run_test.py
# @desc :

import os
import sys
from public import config
rootpath = config.src_path
syspath= sys.path
sys.path=[]
sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)

from base.run_method import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.send_mail import SendMail


class RunTest(object):
    """这是RunTest"""

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.common_util = CommonUtil()
        self.send_email = SendMail()

    def go_on_run(self):
        pass_list = []
        fail_list = []
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            res = None
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_request_data_by_json(i)
            header = self.data.get_header(i)
            expect_result = self.data.get_expect_result(i)
            if is_run == "yes":
                res = self.run_method.run_main(method, url, data, header)
                if self.common_util.is_contain(expect_result, res):
                    print("用例{}测试通过".format(i))
                    pass_list.append(i)
                    self.data.write_actual_result(i, 'PASS')
                else:
                    print("用例{}测试失败".format(i))
                    fail_list.append(i)
                    self.data.write_actual_result(i, res)
                print(res)
        print("=============================")
        print("{}通过".format(len(pass_list)))
        print("{}失败".format(len(fail_list)))
        self.send_email.send_main(pass_list, fail_list)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()




