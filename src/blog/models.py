from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name


class Product(models.Model):
	name  = models.CharField(max_length=100)
	date  = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default="default.png",blank=True)
	subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,default=None)

		
	def __str__(self):
		return self.name	


class Review(models.Model):
	title = models.CharField(max_length=100)
	slug  = models.SlugField()
	body  = models.TextField()
	date  = models.DateTimeField(auto_now_add=True)
	product = models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
	author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
		
	def __str__(self):
		return self.title	

		#function to return post text only 50 characters
	def snippet(self):
		return self.body[:50]+'...'	