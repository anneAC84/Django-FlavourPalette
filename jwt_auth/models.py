from django.db import models
from django.contrib.auth.models import AbstractUser
#from recipes.models import Recipe
#from django.contrib.auth import get_user_model

#User = get_user_model()

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    profile_image=models.URLField(default='http://localhost/placeholder-img.jpg')
    #bookmarks = models.ManyToManyField('recipes.Recipe', related_name='bookmarked_by')
    