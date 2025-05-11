from django import forms
from django.contrib.auth.forms import UserCreationForm,User,AuthenticationForm
from magazin.models import *

class OrderForm(forms.ModelForm):
	class Meta():
		model = Order
		fields = ['adress','telephon','statusdelivery']
    

class ProductfForm(forms.ModelForm):
	class Meta():
		model = Productf
		fields = ['product','productord']

class RegisterUserForm(UserCreationForm):
	username=forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
	email=forms.EmailField(label='Email', widget = forms.EmailInput(attrs={'class': 'form-control'}))
	password1=forms.CharField(label='Пароль', widget = forms.PasswordInput(attrs={'class': 'form-control'}))
	password2=forms.CharField(label='Повтор пароля', widget = forms.PasswordInput(attrs={'class': 'form-control'}))
	adress=forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields = ('username','email','password1','password2','adress')
		
		


class LoginUserForm(AuthenticationForm):
	username=forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control'}))
	password=forms.CharField(label='Пароль', widget = forms.PasswordInput(attrs={'class': 'form-control'}))
	