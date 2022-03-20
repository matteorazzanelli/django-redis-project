from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name = 'home'),
  path('post/<int:pk>/', views.post_detail, name='post_detail'), 
  path('post_list/', views.post_list, name='post_list'),
  path('search/', views.search, name='search'),
  path('help/', views.help, name='help'),
  # post/ means that the URL should begin with the word post
  # <int:pk> It means that Django expects an integer value and will transfer it to a view as a variable called pk
  
]