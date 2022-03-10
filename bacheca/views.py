from django.shortcuts import render, get_object_or_404
from urllib import response
from django.http import JsonResponse
from .models import Post
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.

def home(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'bacheca/post_list.html', {'posts': posts})

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'bacheca/post_detail.html', {'post': post})
  
# def post_list(request):
#   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#   return render(request, 'blog/post_list.html', {'posts': posts})

# def search(request):
#   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#   return render(request, 'blog/post_list.html', {'posts': posts})


# def datetime_posts(requests):
#   response = []
#   posts = Post.objects.filter().order_by('-datetime')
#   for post in posts:
#     response.append(
#       {
#         'datetime': post.datetime,
#         'content': post.content,
#         'author': f"{post.user.first_name} {post.user.last_name}"
#       }
#     )
#   return JsonResponse(response, safe=False)