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
from app01 import views
from django.urls import path
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index),
    url('login', views.login),
    path('home', views.Myview.as_view()),
    url('detail-(\d+).html', views.detaila),
    url('detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detailb),
    url('detail.html', views.detailc),
    url('nametestnametest', views.nametest,name='namename'),
]