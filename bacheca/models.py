from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  datetime = models.DateTimeField(auto_now_add=True)
  birth_date = models.DateField(null=True)
  title_date = models.DateField(null=True)
  vote = models.IntegerField(default=0)
  published_date = models.DateTimeField(blank=True, null=True)
  
  def publish(self):
    self.published_date = timezone.now()
    self.save()
    
  def __str__(self):
    return self.title
  