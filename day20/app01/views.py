from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import json
# Create your views here.

def business(request):
	v1 = models.Business.objects.all()
	# v 是QuerySet,是一个一个的对象
	# [obj(id,caption,code),obj(obj,caption,code)...]

	v2 = models.Business.objects.all().values('id','caption')
	# v 是QuerySet，是一个字典
	# [{'id':1,'caption','运维部'},{'id':2,'caption','销售部'}...]

	v3 = models.Business.objects.all().values_list('id', 'caption')
	# v 是QuerySet，是一个元组
	# [(1,'运维部'),(1,'销售部')...]

	return render(request,'business.html',{'v1':v1,'v2':v2,'v3':v3})

def host(request):
	if request.method == 'GET':
		print('1111111')
		v1 = models.Host.objects.filter(nid__gt=0)
		# for row in v1:
		# 	print(row.nid,row.hostname,row.ip,row.port,row.b_id,row.b)
		#values用来去某一部分的字段，而不是类似*的所有字段,再去关联表的数据时使用双下划綫，而不是"."
		v2 = models.Host.objects.filter(nid__gt=0).values('nid','hostname','b_id','b__caption')

		v3 = models.Host.objects.filter(nid__gt=0).values_list('nid', 'hostname', 'b_id', 'b__caption')

		b_list = models.Business.objects.all()
		return render(request, 'host.html', {'v1': v1, 'v2': v2, 'v3': v3, 'b_list': b_list})
	elif request.method=='POST':
		print('222222')
		h = request.POST.get('hostname')
		i = request.POST.get('ip')
		p = request.POST.get('port')
		b = request.POST.get('b_id')
		models.Host.objects.create(
			hostname = h,
			ip = i,
			port = p,
			b_id = b
		)
		return redirect('/host')


def add_host_ajax(request):
	print('3333333')
	import json
	ret = {'status':True,'error':None,'data':None}
	try:
		h = request.POST.get('hostname')
		i = request.POST.get('ip')
		p = request.POST.get('port')
		b = request.POST.get('b_id')
		print(h,i,p,b)
		if h and len(h)>5:
			models.Host.objects.create(
				hostname=h,
				ip=i,
				port=p,
				b_id=b
			)
		else:
			print('''444444''')
			ret['status']=False
			ret['error']='太短了'
	except Exception as e:
		print('5555555')
		ret['status'] = False
		ret['error'] = '请求错误'
	return HttpResponse(json.dumps(ret))

def edit_host_ajax(request):
	print('6666666')
	import json
	ret = {'status':True,'error':None,'data':None}
	try:
		h_id = request.POST.get('nid')
		h = request.POST.get('hostname')
		i = request.POST.get('ip')
		p = request.POST.get('port')
		b = request.POST.get('b_id')
		print(h_id,h,i,p,b)
		if h and len(h)>5:
			models.Host.objects.filter(nid=h_id).update(
				hostname=h,
				ip=i,
				port=p,
				b_id=b,
			)

		else:
			print('7777777')
			ret['status']=False
			ret['error']='太短了'
	except Exception as e:
		print('8888888')
		ret['status'] = False
		ret['error'] = '请求错误'
	return HttpResponse(json.dumps(ret))

def delete_host(request):
	print('9999999')
	import json
	ret = {'status': True, 'error': None, 'data': None}
	try:
		h_id = request.POST.get('nid')
		print(h_id)
		if h_id:
			models.Host.objects.filter(nid=h_id).delete()

		else:
			print('1010101010')
			ret['status'] = False
			ret['error'] = 'id不存在'
	except Exception as e:
		print('11-11-11')
		ret['status'] = False
		ret['error'] = '请求错误'
	return HttpResponse(json.dumps(ret))


def app(request):
	if request.method == 'GET':
		app_list = models.Application.objects.all()
		host_list = models.Host.objects.all()
		# for row in app_list:
		# 	print(row.name,row.r.all())

		return render(request,'app.html',{'app_list':app_list,'host_list':host_list})
	elif request.method == 'POST':
		#增加数据
		appname = request.POST.get('app_name')
		hostlist = request.POST.getlist('host_list')
		print(appname,hostlist)

		obj = models.Application.objects.create(name = appname)
		obj.r.add(*hostlist)
		return redirect('/app')


def ajax_add_app(request):
	ret = {'status':True,'errro':None,'data':None}
	user = request.POST.get('user')
	pwd = request.POST.get('pwd')
	print(user,pwd)
	return redirect('/app')