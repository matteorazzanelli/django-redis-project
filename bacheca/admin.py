from lib2to3.pgen2.token import EQUAL
from django.contrib import admin
from .models import Post # import model

from .utils import sendTransaction
from django.http import JsonResponse
import hashlib

from .signals.handlers import *

# Register your models here.
# admin.site.register(Post) # to customize admin site behaviour

# Define the admin class
class PostAdmin(admin.ModelAdmin):
  # customize post views
  list_display = ('hash', 'name', 'surname', 'birth_date', 'title_name', 'title_date', 'vote')
  
  # customize save button behaviour
  def save_model(self, request, obj, form, change):
    post = form.save(commit=False)
    jsoncontent = self.JsonfromContent(post) # take the json of the post
    post.hash = str(hashlib.sha256(jsoncontent.content).hexdigest()) # create the hash
    post.txId = sendTransaction(post.hash) # send transaction on ropsten
    post.save() # save the post effectively

  def JsonfromContent(self, post):
    response = []
    response.append(
      {
        'user': str(post.user),
        'name': post.name,
        'surname': post.surname,
        'birth_date': post.birth_date,
        'title_name': post.title_name,
        'title_date': post.title_date,
        'vote': post.vote,
        'published_date': post.published_date
      }
    )
    return JsonResponse(response, safe=False)

# Register the admin class with the associated model
admin.site.register(Post, PostAdmin)
