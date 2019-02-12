from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from blog.models import Category,SubCategory,Review,UserReview
from .forms import userReviewForm
from django.views.generic.edit import FormView
class ReviewListView(ListView):

    model = Review
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        paginate_by = 1
        return context

class ReviewDetailView(DetailView):

    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        key=context['object'].pk
        context['user_reviews'] = UserReview.objects.filter(review=key)
        context['form'] = userReviewForm()
        context['key']= key
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

def search(request):
    if request.method == 'POST':
        reviews = []
        selected_category = request.POST.get('selected_category',None)
        sortby = request.POST.get('sortby',None)
        keyword = request.POST.get('keyword',None)
        print("keyword:"+keyword)
        if selected_category == "all"  and not keyword:
            reviews = Review.objects.all().order_by(sortby)
        elif keyword :
            reviews = Review.objects.filter(title__contains=keyword).order_by(sortby)
            print("run")
        else:
            for review in Review.objects.all().order_by(sortby):
                print(review.product.subcategory.category)
                if review.product.subcategory.category.name == selected_category:
                    print('category matched')
                    reviews.append(review)
                else:
                    print('not matched any category')    

        print(selected_category)
    else:
        reviews = Review.objects.all().order_by('-date')
    categories = Category.objects.all()
    return render(request,'search.html',{'reviews':reviews,'categories':categories})        


class CreateUserReview(FormView):
    #template_name = 'contact.html'
    form_class = userReviewForm
    success_url = '/blog/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        print("submitted")
        return super().form_valid(form)