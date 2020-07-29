#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 23:42
# @Author  : 一叶知秋
# @File    : forms.py
# @Software: PyCharm
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128)
    password=forms.CharField(label='密码',max_length=256,widget=forms.PasswordInput)
