from django.db import models

# Create your models here.
class Newsself(models.Model):
	titel=models.CharField(max_length=255)
	content = models.TextField(blank=True)
	photo =models.ImageField(upload_to='photo=/%Y/%m/%d')
	
	
	def __str__(self):
		return self.titel




class Addphoto(models.Model):
	photo = models.ImageField(upload_to='photo=/%Y/%m/%d')
	addphoto = models.ForeignKey('Newsself',on_delete=models.CASCADE,null=True)
	
	
	
	
		