"""day19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
#如果是多个app功能，则进行分发,引入from django.conf.urls import include，然后如下写

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01', include("app01.urls")),
    path('app02', include("app02.urls")),
]


'''
#只有一个app功能的时候
from app01 import views
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index),
    path('login', views.login),
    path('home', views.Myview.as_view()),
    url('detail-(\d+).html', views.detaila),
    url('detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detailb),
    url('detail.html', views.detailc),
    url('nametestnametest', views.nametest,name='namename'),
]
'''
