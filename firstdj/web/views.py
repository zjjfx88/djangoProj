from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def login(request):
	#直接在浏览器里请求login页面是get请求，这个时候只是返回登录页面
	#在登录页面输入用户名密码，点击登录，post传递用户名密码，则需要在判断用户名密码之后跳转到其他页面
	#或者提示密码错误
	error_msg=''
	if request.method == 'POST':
		#获取post传递过来的数据
		user = request.POST.get('user',None)
		pwd = request.POST.get('pwd', None)
		if user == 'root' and pwd =='123':
			return redirect('/home')
		else:
			error_msg='用户名或者密码错误'
	return render(request,'login.html',{'error_msg':error_msg})

# def login(request):
# 	#第一种方法
# 	# f=open('templates/login.html','r',encoding='utf-8')
# 	# data = f.read()
# 	# f.close()
# 	# return HttpResponse(data)
# 	#django自己的方法
# 	return render(request,'login.html')

def home(request):
	return render(request,'home.html')