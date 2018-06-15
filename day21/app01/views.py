from django.shortcuts import render,HttpResponse,redirect
from utils import pagination
import datetime
# Create your views here.

def auth(func):
	def inner(request,*args,**kwargs):
		v = request.COOKIES.get('username111')
		if not v:
			return redirect('/login')
		return func(request,*args,**kwargs)
	return inner

@auth
def home(request):
	#获取登录用户名
	c = request.COOKIES.get('username111')
	return render(request,'home.html',{'current_user':c})

user_info={
	'user1':{'pwd':'123'}
}
def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	elif request.method == 'POST':
		u = request.POST.get('username')
		p = request.POST.get('passwd')
		dic = user_info.get(u)
		if not dic:
			return render(request,'login.html')
		if dic['pwd'] == p:
			res = redirect('/home')
			#max_age:计时失效，单位秒，expires定时生效
			#取当前时间(utcnow()世界时间)，now()北京时间
			current_time = datetime.datetime.utcnow()
			cookie_expire= current_time + datetime.timedelta(seconds=10)
			#res.set_cookie('username111',u,max_age=10)
			res.set_cookie('username111', u,expires=cookie_expire)
			return res

def index(request,name):
	print(name)
	userlist=[1,2,35,6]
	return render(request,'sub1.html',{'userlist':userlist})


def index2(request):
	name='adaAAAAdafab'
	return render(request,'templatetags.html',{'name':name})


LIST=[]
for i in range(109):
	LIST.append(i)

def user_list(request):
	current_page = request.GET.get('p',1)
	current_page = int(current_page)
	per_count = request.COOKIES.get('per_page_count')
	if per_count is None:
		per_count=10
	else:
		print('aaa',per_count)
		per_count=int(per_count)
	page_obj = pagination.Page(current_page,len(LIST),per_count)
	data = LIST[page_obj.start:page_obj.end]
	page_str = page_obj.page_str("/user_list/")
	return render(request,'user_list.html',{'li':data,'page_str':page_str})