# accounts/urls.py
from django.urls import path

# from .views import CategoryListView
from . import views

urlpatterns = [
    path('categories', views.get_categories, name='all_categories'),
    path('', views.ReviewListView.as_view(), name='all_reviews'),
    path('<slug:slug>/', views.ReviewDetailView.as_view(), name='review-detail'),
]