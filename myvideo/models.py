from django.db import models

# Create your models here.

class Vidos(models.Model):
	video = models.FileField(upload_to='video=/%Y/%m/%d')
	content = models.TextField(blank=True)

