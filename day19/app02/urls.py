#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangjingjun'
__mtime__ = '2018/2/8'
# ----------Dragon be here!----------
              ┏━┓      ┏━┓
            ┏━┛ ┻━━━━━━┛ ┻━━┓
            ┃       ━       ┃
            ┃  ━┳━┛   ┗━┳━  ┃
            ┃       ┻       ┃
            ┗━━━┓      ┏━━━━┛
                ┃      ┃神兽保佑
                ┃      ┃永无BUG！
                ┃      ┗━━━━━━━━━┓
                ┃                ┣━┓
                ┃                ┏━┛
                ┗━━┓ ┓ ┏━━━┳━┓ ┏━┛
                   ┃ ┫ ┫   ┃ ┫ ┫
                   ┗━┻━┛   ┗━┻━┛
"""
from django.contrib import admin
from app02 import views
from django.urls import path
from django.conf.urls import url
urlpatterns = [
    url('login', views.login),
    url('orm', views.orm),
    url('index', views.index),
    url('user_info', views.user_info),
    url('datail-(?P<nid>\d+)', views.user_detail),
    url('del-(?P<nid>\d+)', views.user_del),
    url('edit-(?P<nid>\d+)', views.user_edit),
    url('group_add', views.group_add),
]