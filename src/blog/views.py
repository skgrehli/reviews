from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from blog.models import Category,SubCategory

class CategoryListView(ListView):

    model = Category
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
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