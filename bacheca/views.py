# from django.shortcuts import render
from urllib import response
from django.http import JsonResponse
from .models import Post
# Create your views here.

def datetime_posts(requests):
  response = []
  posts = Post.objects.filter().order_by('-datetime')
  for post in posts:
    response.append(
      {
        'datetime': post.datetime,
        'content': post.content,
        'author': f"{post.user.first_name} {post.user.last_name}"
      }
    )
  return JsonResponse(response, safe=False)
