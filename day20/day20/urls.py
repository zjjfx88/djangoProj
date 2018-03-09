"""day20 URL Configuration

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
from django.urls import path,re_path,include
from app01 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01', include("app01.urls")),
    re_path(r'^business$', views.business),
    re_path(r'^host', views.host),
    re_path(r'^add_host_ajax', views.add_host_ajax),
    re_path(r'^edit_host_ajax', views.edit_host_ajax),
    re_path(r'^delete_host',views.delete_host),
    re_path(r'^app$',views.app),
    re_path(r'^ajax_add_app$',views.ajax_add_app),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
