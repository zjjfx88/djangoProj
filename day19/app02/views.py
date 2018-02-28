from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else:
		u = request.POST.get('username')
		p = request.POST.get('password')
		#.first命中条件的所有数据中的第一条，.count符合条件的条数
		obj = models.UserInfo.objects.filter(username=u,password=p).first()
		if obj:
			print("yes")
			return redirect('/app02/index')
		else:
			print("no")
			return render(request,'login.html')


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
	#models.UserInfo.objects.filter(username='zhangjj').update(password='123')

	#一对多
	#user_list = models.UserInfo.objects.all()
	user_list = models.UserInfo.objects.create(
		username = 'root1',
		password = '123',
		email = 'zjj@163.com',
		user_group_id = 1
	)
	return HttpResponse('orm')

def index(request):
	return render(request,'index.html')

def user_info(request):
	if request.method == 'GET':
		# 打印实际执行的query使用userlist.query
		userlist=models.UserInfo.objects.all()
		for row in userlist:
			print(row.id)
			print(row.user_group.uid)
		grouplist = models.UserGroup.objects.all()

		return render(request,'user_info.html',{'user_list':userlist,'group_list':grouplist})
	else:
		user = request.POST.get('username')
		pwd = request.POST.get('password')
		groupid = request.POST.get('group_id')
		models.UserInfo.objects.create(
			username=user,
			password=pwd,
			user_group_id=groupid,
		)
		return redirect('/app02/user_info')

def user_info_b(request):
	if request.method == 'GET':
		# 打印实际执行的query使用userlist.query
		userlist=models.UserInfo.objects.all()
		# for row in userlist:
		# 	print(row.id)
		# 	print(row.user_group.uid)
		grouplist = models.UserGroup.objects.all()

		return render(request,'user_info_b.html',{'user_list':userlist,'group_list':grouplist})
	else:
		user = request.POST.get('username')
		pwd = request.POST.get('password')
		groupid = request.POST.get('group_id')
		models.UserInfo.objects.create(
			username=user,
			password=pwd,
			user_group_id=groupid,
		)
		return redirect('/app02/user_info_b')


def user_detail(request,nid):
	userdetail=models.UserInfo.objects.filter(id=nid).first()
	#取单条数据也可以使用get，但是如果不存在会报错，所以使用get的时候需要进行try catch
	#userdetail = models.UserInfo.objects.get(id=nid)
	#print(userdetail)
	return render(request,'user_detail.html',{'user_detail':userdetail})

def user_del(request,nid):
	models.UserInfo.objects.filter(id=nid).delete()
	return redirect('/app02/user_info')

def user_edit(request,nid):
	if request.method == 'GET':
		user=models.UserInfo.objects.filter(id=nid).first()
		return render(request,'user_edit.html',{'user':user})
	elif request.method == 'POST':
		user = request.POST.get('username')
		pwd = request.POST.get('password')
		models.UserInfo.objects.filter(id=nid).update(username=user,password=pwd)
		return redirect('/app02/user_info')

def group_add(request):
	models.UserGroup.objects.create(caption='测试组')
	return render(request,'/app02/user_info')