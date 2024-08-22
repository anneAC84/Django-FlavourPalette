#from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
#from recipes.models import Recipe

class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    profile_image=models.URLField(default='http://localhost/placeholder-img.jpg')
    #bookmarks = models.ManyToManyField(Recipe, related_name='bookmarked_by')
    