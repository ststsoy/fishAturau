from django.contrib import admin

# Register your models here.
from .models import*

class OrderInline(admin.StackedInline):
	model = Productf
	extra = 2

class OrderAdmin(admin.ModelAdmin):
	field ='__all_'
	inlines = [OrderInline]





class BassketAdmin(admin.ModelAdmin):
	field ='__all_'
	list_display=['product','images']
	



admin.site.register(Order,OrderAdmin)
admin.site.register(Statusdelivery)
admin.site.register(Product)
admin.site.register(Productf)
admin.site.register(Bassket,BassketAdmin)

