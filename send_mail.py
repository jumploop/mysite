#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 12:37
# @Author  : 一叶知秋
# @File    : send_mail.py
# @Software: PyCharm

import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
if __name__ == '__main__':
    message = '欢迎访问https://www.zhihu.com/people/rather_critical，这里是一叶知秋的知乎账号，欢迎关注我！'
    send_mail('来自一叶知秋的测试邮件', message, 'xxxxxwwdd@sina.com',
              ['xxxxxx@qq.com', 'xxxxxx@gmail.com', 'xxxxxxxx@gmail.com'])
