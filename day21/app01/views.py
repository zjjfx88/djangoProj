from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request,name):
	print(name)
	userlist=[1,2,35,6]
	return render(request,'sub1.html',{'userlist':userlist})


def index2(request):
	name='adaAAAAdafab'
	return render(request,'index2.html',{'name':name})