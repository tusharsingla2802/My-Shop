from django.contrib import admin
from .models import Category,Product
# Register your models here.
@admin.register(Category)
class Category(admin.ModelAdmin):
     list_diasplay=['name','slug']
     prepopulated_feilds={'slug':('name',)}
@admin.register(Product)
class Product(admin.ModelAdmin):
     list_display=['name','slug','price','available','created','updated']
     list_filter=['available','created','updated']
     list_editable=['price','available']
     prepopulated_fields={'slug':('name',)}
     
