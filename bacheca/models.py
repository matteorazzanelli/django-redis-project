from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  surname = models.CharField(max_length=100)
  birth_date = models.DateField(null=True)
  title_name = models.CharField(max_length=100)
  title_date = models.DateField(null=True)
  vote = models.IntegerField(null=True, default=0)
  published_date = models.DateTimeField(null=True)
  hash = models.CharField(max_length=64, default=None, null=True, blank=True)
  txId = models.CharField(max_length=66, default=None, null=True, blank=True)
  
  def publish(self):
    self.published_date = timezone.now()
    self.save()
    
  def __str__(self):
    return self.name + ' ' + self.surname + ' ' + str(self.title_date)