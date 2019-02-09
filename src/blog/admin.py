from django.contrib import admin
from .models import Product,Category,SubCategory,Review,RPros,Cons,UserReview


# Register your models here.
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(RPros)
admin.site.register(Cons)
admin.site.register(UserReview)
# admin.site.register(Rating)
