from django.shortcuts import render, redirect ,get_object_or_404
from  .models import*
# Create your views here.
def video(request):
	video = Vidos.objects.all()
	return render(request,'myvideo/video.html',{'video':video})
