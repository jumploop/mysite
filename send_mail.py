#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 12:37
# @Author  : 一叶知秋
# @File    : send_mail.py
# @Software: PyCharm

import os
from django.core.mail import send_mail, EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
if __name__ == '__main__':
    # message = '欢迎访问https://www.zhihu.com/people/rather_critical，这里是一叶知秋的知乎账号，欢迎关注我！'
    # send_mail('来自一叶知秋的测试邮件', message, 'ggggggss@sina.com',
    #           ['xxxxx@qq.com', 'xxxxxxx@gmail.com', 'dddddd@gmail.com'])
    subject, from_email, to = '来自一叶知秋的测试邮件', 'xxxx@sina.com', 'xxxxx@qq.com'
    text_content = '欢迎访问https://www.zhihu.com/people/rather_critical，这里是一叶知秋的知乎账号，欢迎关注我！'
    html_content = '<p>欢迎访问<a href="https://www.zhihu.com/people/rather_critical" target=blank>https://www.zhihu.com/people/rather_critical</a>，这里是一叶知秋的知乎账号，欢迎关注我！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
