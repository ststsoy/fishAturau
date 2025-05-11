from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
	image = models.ImageField(upload_to ='users_images',blank=True)
	adress = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)


