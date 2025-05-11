from django.urls import path
from .import views

urlpatterns = [
               path('add/',views.addphoto,name='addphoto'),
               path('newsself/<int:id_new>',views.newsself,name='newsself'),
               path('newsselfs',views.newsselfs,name='newsselfs'),
               ]
               