from django.contrib import admin
from newsself.models import Newsself,Addphoto

# Register your models here.


class NewsselfInline(admin.StackedInline):
    model = Addphoto 
    extra = 1

class NewsselfAdmin(admin.ModelAdmin):
    fields = ['titel','content','photo']
    inlines = [NewsselfInline]



admin.site.register(Newsself,NewsselfAdmin)
admin.site.register(Addphoto)