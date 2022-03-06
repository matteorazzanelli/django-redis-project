from django.contrib import admin
from .models import Post # import model

# Register your models here.
# Per poter accedere al nuovo modello dal pannello di controllo...
admin.site.register(Post)

