from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def login(request):
	return HttpResponse("<h1>app02 login</h1>")


from app02 import models
def orm(request):
	#增
	# #插入数据的方式一
	# models.UserInfo.objects.create(
	# 	username='root',
	# 	password='123'
	# )
	# #插入方式二
	# obj=models.UserInfo(username='zhangjj',
	# 	password='123',)
	# obj.save()
	#
	# #插入方式三
	# user_dict={'username':'zjj','password':'123'}
	# models.UserInfo.objects.create(**user_dict)

	#查全部
	#result = models.UserInfo.objects.all()
	#查过滤查username是root且password是123的
	# result = models.UserInfo.objects.filter(username='root',password='123')
	# for row in result:
	# 	print(row.id,row.username)


	#删除全部
	#models.UserInfo.objects.all().delete()
	#删除某条
	#models.UserInfo.objects.filter(username='zjj').delete()

	#更新全部
	# models.UserInfo.objects.all().update(password='666')
	#更新某条
	models.UserInfo.objects.filter(username='zhangjj').update(password='123')
	return HttpResponse('orm')