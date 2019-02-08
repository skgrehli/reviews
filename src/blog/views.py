from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from blog.models import Category,SubCategory,Review,UserReview
from .forms import userReviewForm
class ReviewListView(ListView):

    model = Review
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ReviewDetailView(DetailView):

    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        key=context['object'].id
        context['user_reviews'] = UserReview.objects.filter(review=key)
        context['form'] = userReviewForm()
        # print()
        return context

        


def get_categories(request):
    categories = []
    subcategories = []
    for category in Category.objects.all():
        categories.append(category)
        for subcategory in SubCategory.objects.filter(category=category):
            subcategories.append({'category':category,'subcategory':subcategory})
    print(subcategories)
    return render(request,'blog/category_list.html',{'categories':categories,'subcategories':subcategories})
    # return render(request,'main/popularpeople.html',{'popularity':popularity})    



def IndexPageView(request):
    categories = []
    subcategories = []
    for category in Category.objects.all():
        categories.append(category)
        for subcategory in SubCategory.objects.filter(category=category):
            subcategories.append({'category':category,'subcategory':subcategory})
    
    reviews = Review.objects.all().order_by('-date')
    reviews_by_views = Review.objects.all().order_by('-views')
    reviews_by_rating = Review.objects.all().order_by('-rating')
    return render(request,'home.html',{'categories':categories,'subcategories':subcategories,'reviews':reviews,'reviews_by_views':reviews_by_views,'reviews_by_rating':reviews_by_rating})
        
