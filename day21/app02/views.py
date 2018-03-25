from django.shortcuts import render,HttpResponse
from django.urls import reverse

# Create your views here.
def detail(request,pk):
	print('111' + request.path_info)
	print(request.resolver_match)
	v = reverse('app02:detail', kwargs={'pk': 11})
	print(v)
	return HttpResponse(pk)


def testurl(request):
#	return HttpResponse('Ok')
	print('000'+request.path_info)
	print(request.environ)
	return render(request,'testurl.html')


def index(request,name):
	print(name)

	return HttpResponse('Ok')