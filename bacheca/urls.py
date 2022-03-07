from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name = 'home'),
  path('posts', views.post_list, name = 'title_list'),
  path('search', views.search, name = 'title_search')
]