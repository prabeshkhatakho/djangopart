from django.urls import path
from .views import Index
from.views import article_list, article_details

urlpatterns = [
    path('', Index, name='Index'),
    path('articles', article_list, name='article'),
    path('articles/<int:pk>/', article_details, name='article_details'),
    
]