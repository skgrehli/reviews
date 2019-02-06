# accounts/urls.py
from django.urls import path

from .views import CategoryListView
from . import views

urlpatterns = [
    path('', views.get_categories, name='all_categories'),
]