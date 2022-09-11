from django.contrib import admin
from shop.models import *
# Register your models here.



class ProductDetails(admin.ModelAdmin):
    list_display = [
        "name",
        "weight",
        "price",
        "category",
    ]

class OrderDetails(admin.ModelAdmin):
    list_display = [
        "user",
        "address",
        "total",
        "note",
        "ref_code",
    ]

class CategoryDetails(admin.ModelAdmin):
    list_display = [
        "parent",
        "name",
        "is_active"
    ]  
    

admin.site.register(Product, ProductDetails)    
admin.site.register(Order, OrderDetails)
admin.site.register(Item)
admin.site.register(Category, CategoryDetails)
admin.site.register(City)
admin.site.register(Town)
admin.site.register(Address)
#admin.site.register()
