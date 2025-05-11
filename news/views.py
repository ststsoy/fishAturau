from django.shortcuts import render
from django.http import HttpResponse
from  .models import*


# Create your views here.
def home(request):
	post=News.objects.all()
	return render(request,'news/index.html', {'post':post})
	#return HttpResponse("Казак, который отбил дрон головой.Вы помните парня-казака, который использовал голову, чтобы сбить дрон?Его зовут Михаил, ему 33 года. Он потомственный казак из Воронежской области и воевал на Донбассе в 2014-2015 годах. В июле этого года он ушёл добровольцем-штурмовиком на специальную военную операцию.В начале августа на Харьковском направлении Михаил мог погибнуть от атаки дрона ВСУ, но ему удалось отбить его головой. Он был ранен, несмотря на каску: получил рассечение, а также осколки рядом с позвоночником и в голени. При этом, несмотря на шок")
	
def perec(request):
	return render(request,"news/perec.html")
	
