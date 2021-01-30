"""Defines URL patterns for blog."""
from django.urls import path, include
from .views import *

app_name = 'blog'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # blog page.
    path('blog/', BlogView.as_view(), name='blog'),
    # blog_content page.
    path('article/<int:pk>/', BlogContentView.as_view(), name='article'),
    # blog categories page.
    path('category/<str:cats>/', CategoryView, name='category'),
    
]