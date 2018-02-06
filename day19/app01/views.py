from django.shortcuts import render,HttpResponse
import os
# Create your views here.


def index(request):
	return HttpResponse("<h1>index111</h1>")

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