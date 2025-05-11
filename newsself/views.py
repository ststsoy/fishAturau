from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect ,get_object_or_404
from newsself.models import Newsself,Addphoto
from newsself.forms import AddphotoForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def newsselfs(request):
	news=Newsself.objects.all()
	addph = Addphoto.objects.all()
	form = AddphotoForm()
	return render(request,'newsself/newsselfs.html',{'news':news,'addph':addph,'form':form})

def newsself(request,id_new):
	news=Newsself.objects.get(id=id_new)
	addph = Addphoto.objects.filter(addphoto=id_new)
	
	return render(request,'newsself/newsself.html',{'news':news,'addph':addph})




def addphoto(request):

	if request.method=='POST':
		form =AddphotoForm(request.POST,request.FILES)
		if form.is_valid():
		
				form.save()
				return redirect('newsselfs')
			

	else:
		form =AddphotoForm()
	return render(request,'newsself/newsselfs.html',{'form':form})