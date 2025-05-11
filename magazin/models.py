from django.db import models
from users.models import User
# Create your models here.
from django.utils.safestring import mark_safe
class Product(models.Model):
	product = models.CharField(max_length=255)
	description = models.TextField(blank = True)
	photo =models.ImageField(upload_to = "photos=/%Y/%m/%d")
	barcode = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=50, decimal_places=2,default=0)


	def __str__(self):
		return self.product
	

#халаява
class Productf(models.Model):
	product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
	productord=models.ForeignKey('Order',on_delete=models.CASCADE,null=True)
	quantity = models.PositiveIntegerField(default=0,null=True)
	create_timestap = models.DateTimeField(auto_now_add=True)


	def	sum(self):
		return self.quantity*self.product.price


	
class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	email = models.EmailField()
	adress = models.CharField(max_length=255)
	telephon = models.CharField(max_length=255) 
	statusdelivery=models.ForeignKey('Statusdelivery',blank = True,on_delete=models.PROTECT,null=True)

    
	

class Statusdelivery(models.Model):
	name=models.CharField(max_length=255)


	def __str__(self):
		return self.name



class Bassket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_timestap = models.DateTimeField(auto_now_add=True)

    def im(self):
    	return self.product.photo.url


    def images(self):
    	return mark_safe('<img src="%s" width="50" height="50" />' % self.im())
    
    def __str__(self):
    	return f'Корзина для {self.user.username}|Продукт {self.product.product}' f'<img src="images()" width="50" height="60"/>'

    def	sum(self):
    	return self.quantity*self.product.price

   