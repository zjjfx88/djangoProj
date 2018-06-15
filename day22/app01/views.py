from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def login(request):
	if request.method=='GET':
		return render(request,'login.html')
	elif request.method=='POST':
		user = request.POST.get('username')
		pwd = request.POST.get('passwd')
		if user =='zhangjj' and pwd == '123':
			#生成随机字符串
			#写到浏览器cookies
			#保存到服务端session中
			# request.session.clear_expired()
			request.session['username'] = user
			request.session['is_login'] = True
			if request.POST.get('rmb',None)==1:
				request.session.set_expiry(10)
			return redirect('/index')
		else:
			return redirect('/login')

def index(request):
	if request.session.get('is_login',None):
		user = request.session['username']
		s_key = request.session.session_key
		print(s_key)
		return render(request,'index.html',{'username':user})
	else:
		return  HttpResponse('get out')

def logout(request):
	# request.session.clear()
	request.session.delete(request.session.session_key)
	return redirect('/login')
