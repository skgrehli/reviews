from django.contrib import admin
from .models import Product,Category,SubCategory,Review

# Register your models here.
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Review)
admin.site.register(Category)

