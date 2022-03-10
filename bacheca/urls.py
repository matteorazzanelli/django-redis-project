from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name = 'home'),
  path('post/<int:pk>/', views.post_detail, name='post_detail'), 
  # post/ means that the URL should begin with the word post
  # <int:pk> It means that Django expects an integer value and will transfer it to a view as a variable called pk
  
  # path('posts', views.post_list, name = 'title_list'),
  # path('search', views.search, name = 'title_search'),
]