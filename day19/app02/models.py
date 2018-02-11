from django.db import models

# Create your models here.

#表名app02_userinfo
class UserInfo(models.Model):
	#
	username = models.CharField(max_length=40)
	password = models.CharField(max_length=64)