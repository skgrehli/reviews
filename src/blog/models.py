from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from embed_video.fields import EmbedVideoField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name+' - '+self.category.name


class Product(models.Model):
	name  = models.CharField(max_length=100)
	date  = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default="default.png",blank=True)
	subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,default=None)

		
	def __str__(self):
		return self.name	


class RPros(models.Model):
    text = models.CharField(max_length=100)
    

    def __str__(self):
        return self.text


class Cons(models.Model):
    text = models.CharField(max_length=100)
    

    def __str__(self):
        return self.text


class Review(models.Model):
	title = models.CharField(max_length=100)
	slug  = models.SlugField()
	body  = models.TextField()
	date  = models.DateTimeField(auto_now_add=True)
	product = models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
	author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	video_url = EmbedVideoField(default="https://www.youtube.com/watch?v=QohH89Eu5iM")
	rpros = models.ManyToManyField(RPros)
	rcons = models.ManyToManyField(Cons)
	comfort=models.IntegerField(default=1,validators=[MaxValueValidator(100), MinValueValidator(1)],null=True)
	price=models.IntegerField(default=1,validators=[MaxValueValidator(100), MinValueValidator(1)],null=True)
	availability=models.IntegerField(default=1,validators=[MaxValueValidator(100), MinValueValidator(1)],null=True )
	support=models.IntegerField(default=1,validators=[MaxValueValidator(100), MinValueValidator(1)],null=True)
	views = models.IntegerField(default=0)
	rating = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(1)],null=True)


    
    

	def __str__(self):
		return self.title	

		#function to return post text only 50 characters
	def snippet(self):
		return self.body[:50]+'...'	



class UserReview(models.Model):
	review = models.ForeignKey(Review,on_delete=models.CASCADE,default=None)
	rating = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(1)])
	comment= models.TextField()
	name = models.CharField(max_length=50)
	email = models.EmailField()
	date  = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name+' - '+self.review.title