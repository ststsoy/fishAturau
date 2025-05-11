from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponse
from magazin.forms import OrderForm,ProductfForm,RegisterUserForm,LoginUserForm
from django.urls import reverse_lazy
from  .models import*
from django.views.generic import CreateView,ListView,DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout,login



# Create your views here.

@login_required
def products(request):
	post=Product.objects.all()
	basket = Bassket.objects.filter(user=request.user)
	total_quantity=0
	for b in basket:
		
		total_quantity+=b.quantity
	return render(request,'magazin/products.html', {'post':post,'total_quantity':total_quantity})
@login_required
def product(request,pro_id):
	post=Product.objects.get(id=pro_id)
	basket = Bassket.objects.filter(user=request.user)
	total_quantity=0
	for b in basket:
		
		total_quantity+=b.quantity

	return render(request,'magazin/product.html',{'post':post,'total_quantity':total_quantity})

@login_required
def orders(request):
	post=Order.objects.filter(user=request.user)
	return render(request,'magazin/orders.html',{'post':post})
@login_required	
def order(request,ord_id):
	post=Order.objects.get(id=ord_id)
	orp=Productf.objects.filter(productord=ord_id)
	pform = ProductfForm()
	total_sum=0
	total_quantity=0
	for o in orp:
		total_sum+=o.sum()
		total_quantity+=o.quantity
	return render(request,'magazin/order.html',{'post':post,'orp':orp,'pform':pform,'total_sum':total_sum,'total_quantity':total_quantity})

def orderf(request):
	form = OrderForm()
	pform = ProductfForm()
	return render(request,'magazin/form.html',{'form':form,'pform':pform})

def addorder(request):

	post=Order.objects.all()
	if request.method=='POST':
		form =OrderForm(request.POST)
		if form.is_valid():
		        form.save()
		        return redirect('/magazin/ord/')
	else:
         form =OrderForm()
	return render(request,'magazin/orders.html',{'post':post})



# def addorderfrombasket(request):
# 	Order.objects.create(email=user.email)




def addprof(request,ord_id):
	orp=Productf.objects.filter(productord=ord_id)
	if request.method=='POST':
		form =ProductfForm(request.POST)
		if form.is_valid():
			
			
			form.save()
			return redirect('/magazin/ord/' )
	else:
         form =ProductfForm()
	return render(request,'magazin/order.html',{'orp':orp})






class RegisterUser(CreateView):
	form_class = RegisterUserForm
	template_name = 'magazin/register.html'
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		user = form.save()
		login(self.request,user)
		return redirect('products')


class LoginUser(LoginView):
	form_class = LoginUserForm
	template_name = 'magazin/login.html'


	def get_success_url(self):
		return reverse_lazy('products')





def logout_user(request):
	logout(request)
	return redirect('login')


@login_required
def basket(request):
	basket = Bassket.objects.filter(user=request.user)
	pform = OrderForm()
	total_sum=0
	total_quantity=0
	for b in basket:
		total_sum+=b.sum()
		total_quantity+=b.quantity
	return render(request,'magazin/baskets.html',{'basket': basket,'total_sum':total_sum,'total_quantity':total_quantity})


def addorderfrombasket(request):
	ord=Order.objects.create(user=request.user,email=request.user.email,adress=request.user.adress,telephon=request.user.phone)
	
	basket = Bassket.objects.filter(user=request.user)
	


	return redirect('/magazin/ord/%d' %ord.id)


def addorderfromforordbasket(request,id_ord):
	ord=Order.objects.get(id=id_ord)
	basket = Bassket.objects.filter(user=request.user)
	productfo = Productf.objects.filter(productord=ord)
	productfo2 = Productf.objects.all()
	for b in basket:
		
		# if not productfo.exists():
			Productf.objects.create(product=b.product,productord=ord,quantity=b.quantity)
			

		# else:
		# 	productfo2=productfo.first()
		# 	productfo2.quantity+=1
		# 	productfo2.save()
			



	return redirect('/magazin/ord/%d' %id_ord)



	

@login_required
def basket_add(request,product_id):
	product = Product.objects.get(id=product_id)
	baskets = Bassket.objects.filter(user=request.user, product=product)
	basket = Bassket.objects.all()
	if not baskets.exists():
		Bassket.objects.create(user=request.user,product=product,quantity=1)
		return redirect('/magazin/basket')
	else:
		basket=baskets.first()
		basket.quantity+=1
		basket.save()
		return redirect('/magazin/basket')

@login_required				
def basket_deleted(request,id):
	basket = Bassket.objects.get(id=id)
	basket.delete()
	return redirect('/magazin/basket')

def clear_baskets(request):
	baskets = Bassket.objects.filter(user=request.user)
	for b in baskets:
		b.delete()


	return redirect('/magazin/basket')
