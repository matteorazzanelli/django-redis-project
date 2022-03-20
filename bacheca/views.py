from django.shortcuts import render, get_object_or_404
from urllib import response
from .models import Post
from django.utils import timezone
from django.shortcuts import redirect
from .forms import PostForm


# Create your views here.

def home(request):
  return render(request, 'bacheca/home.html', {})

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'bacheca/post_detail.html', {'post': post})
  
def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'bacheca/post_list.html', {'posts': posts})

def search(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      # Try to find the post with the title name
      try:
        pk = Post.objects.get(title_name=post.title_name).pk
      # Error 404 if it does not exist instead of an exception
      except Post.DoesNotExist:
        pk = 0
      return redirect('post_detail', pk=pk)
  else:
    form = PostForm()
  return render(request, 'bacheca/search.html', {'form': form})

def help(request):
  return render(request, 'bacheca/help.html', {})

# def newPost(request):
#   if request.method == "POST":
#     form = Post(request.POST)
#     if form.is_valid():
#       post = form.save(commit=False)
#       post.author = request.user
#       post.published_date = timezone.now()
#       post.save()
#       # post = Post.objects.filter()[0]
#       post.writeOnChain()
#       # return redirect('post_detail', pk=post.pk)
#   else:
#     form = Post()
#   return render(request, 'blog/post_edit.html', {'form': form})