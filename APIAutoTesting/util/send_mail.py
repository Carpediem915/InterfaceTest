#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/2/27 09:30 
# @Author : hcm 
# @File : send_mail.py
# 

import smtplib
from email.mime.text import MIMEText


class SendMail(object):
    """这是SendMail"""
    global email_host
    global username
    global password

    email_host = "smtp.163.com"
    username = "carpediem915@163.com"
    password = "hcm19920915"  # 邮箱客户端授权码，非邮箱密码

    def send_mail(self, sub, to_list, content):
        sender = "hcm" + "<" + username + ">"

        message = MIMEText(content, _charset='utf-8')
        message['Subject'] = sub
        message['From'] = sender
        message['To'] = ";".join(to_list)

        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(username, password)
        server.sendmail(sender, to_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        count_num = pass_num + fail_num
        pass_percent = "%.2f%%" % (pass_num / count_num * 100)
        fail_percent = "%.2f%%" % (fail_num / count_num * 100)
        subject = '接口自动化'
        to_list = ['630134082@qq.com']
        content = "此次一共运行%d个接口，通过%d个，失败%d个，通过率为%s，失败率为%s" % (count_num, pass_num, fail_num, pass_percent, fail_percent)
        self.send_mail(subject, to_list, content)
        pass


if __name__ == '__main__':
    send = SendMail()
    # subject = '接口自动化'
    # to_list = ['630134082@qq.com']
    # content = "这是一封测试邮件"
    pass_list = [1,2,3,4]
    fail_list = [5,6]
    send.send_main(pass_list, fail_list)
