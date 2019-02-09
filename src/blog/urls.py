# accounts/urls.py
from django.urls import path

# from .views import CategoryListView
from . import views

urlpatterns = [
    path('categories', views.get_categories, name='all_categories'),
    path('', views.ReviewListView.as_view(), name='all_reviews'),
    path('createUserReview/', views.CreateUserReview.as_view(), name='my_form_view_url'),
    path('search/',views.search,name='search'),
    path('<slug:slug>/', views.ReviewDetailView.as_view(), name='review-detail'),
]