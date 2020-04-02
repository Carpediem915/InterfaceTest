#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/2/20 16:39 
# @Author : hcm 
# @File : test_method.py
# @desc :
import unittest
import mock
from base.demo import RunMain
from base.mock_demo import mock_test
from HTMLTestRunner import HTMLTestRunner


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def tearDown(self):
        pass

    def test_01(self):
        url = 'http://127.0.0.1:8000/getuser/'
        data = {
            'id': '001'
        }
        # 模拟返回数据
        test_data = {'errorCode': 0, 'username': '测试数据'}
        res = mock_test(self.run.run_main, url, 'GET', data, test_data)

        # res = self.run.run_main(url, 'GET', data)
        self.assertEqual(res['errorCode'], 0)

    # 在类里面定义全局变量
    # globals()['userid'] = 100001
    # 跳过此条用例
    # @unittest.skip
    def test_02(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': 'hcm',
            'password': '1234'
        }
        # 使用全局变量
        # print(userid)

        # 模拟返回数据
        test_data = {'errorCode': 0, 'user': '测试测试', 'pwd': '1234'}
        res = mock_test(self.run.run_main, url, 'POST', data, test_data)

        # res = self.run.run_main(url, 'POST', data)

        print(res)
        self.assertEqual(res['errorCode'], 0)


if __name__ == '__main__':
    # 默认执行方法，全部用例都会被执行
    # unittest.main(verbosity=2)

    # 通过测试组件选择性执行用例
    # 1. 创建测试组件
    suite = unittest.TestSuite()
    # 2. 加载测试用例到测试组件
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    # 3. 实例化TextTestRunner执行用例并显示结果
    unittest.TextTestRunner().run(suite)

    # 3. 使用第三方库HTMLTestRunner输出测试报告,导出成html文件，方便查看
    # filePath = '../report/html_report.html'
    # with open(filePath, 'wb') as f:
    #     pass
    #     runner = HTMLTestRunner(stream=f, title='Imooc接口测试报告', description='登录和获取用户信息')
    #     runner.run(suite)
