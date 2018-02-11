from django.shortcuts import render,HttpResponse
import os
# Create your views here.
USER_DICT={
	'1':{'name':'root1','email':'root@live.com'},
	'2':{'name':'root2','email':'root@live.com'},
	'3':{'name':'root3','email':'root@live.com'},
	'4':{'name':'root4','email':'root@live.com'},
	'5':{'name':'root5','email':'root@live.com'},
}

def nametest(request):
	if request.method=='POST':
		return HttpResponse('<h1>name post</h1>')
	else:
		return render(request,'nametest.html')


#正则匹配的多参数url---url('detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
#不使用?P<nid>，则方法按照顺序定义形参，使用?P<nid>则不需要按照顺序
def detailb(request,uid,nid):
	print(nid,uid)
	detail_info = USER_DICT[nid]
	return render(request, 'detail.html', {'detail': detail_info})


#正则匹配的单url---url('detail-(\d+).html', views.detail),
def detaila(request,nid):
	detail_info=USER_DICT[nid]
	return render(request,'detail.html',{'detail':detail_info})

#普通方式的url---path('detail', views.detail)
def detailc(request):
	key=request.GET.get('nid')
	detail_info=USER_DICT[key]
	return render(request,'detail.html',{'detail':detail_info})




def index(request):
	return render(request,'index.html',{'user_list':USER_DICT})

def login(request):
	if request.method == 'POST':
		# #获取性别Radio
		# gender=request.POST.get('gender')
		# print(gender)
		#
		# #获取checkbox的值
		# favor=request.POST.getlist('favor')
		# print(favor)
		#
		# #获取select的值，单选用get，多选用getlist
		# city=request.POST.getlist('city')
		# print(city)

		#只能取到post提交的文件名
		v = request.POST.get('fafafa')
		print(v)
		#给form增加enctype="multipart/form-data"可用来传递文件，此时无法从post里活得文件名，可以通过
		#post传递的FILES里面获取文件名，文件内容等

		obj=request.FILES.get('fafafa')
		file_path = os.path.join('upload', obj.name)
		f=open(file_path,mode='wb')
		for i in obj.chunks():
			f.write(i)
		f.close()
		return render(request, 'login.html')
	elif request.method=='GET':
		return render(request,'login.html')



#上面都是在views中定义函数，用来相应http请求，下面则是在views中定义类，使用类进行相应,这样需要类继承views
#在urls.py中添加映射path('home', views.Myview.as_view())
#原理：通过继承view类，在请求来了之后会先执行dispatch方法来获取请求的类型是get还是post或者其他
#如果想在调用get和post方法之前添加操作，可以在dispartch中添加，但是为了不影响dispatch的功能，则需要
#使用super方法,可以在每次请求前后添加处理方法，即before和after的地方
from django.views import View
class Myview(View):
	def dispatch(self, request, *args, **kwargs):
		print('before')
		result=super(Myview,self).dispatch(request,*args,**kwargs)
		print('after')
		return result

	def get(self,request, *args, **kwargs):
		print(request.method)
		#print(request.GET)
		return render(request,'classMode.html')

	def post(self,request, *args, **kwargs):
		print(request.method)
		return render(request,'classMode.html')