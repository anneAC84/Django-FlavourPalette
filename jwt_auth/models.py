from django.db import models
from django.contrib.auth.models import AbstractUser
#from recipes.models import Recipe
#from django.contrib.auth import get_user_model

#User = get_user_model()

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    profile_image=models.URLField(default='https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/thumbnails/image/placeholder-profile_1.png')
    #bookmarks = models.ManyToManyField('recipes.Recipe', related_name='bookmarked_by')
    