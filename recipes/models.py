from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Recipe(models.Model):
    title = models.CharField(max_length=50)
    picture = models.URLField(default='http://localhost/placeholder-img.jpg')
    description = models.TextField(max_length=100)
    ingredients = models.TextField(max_length=500)
    method = models.TextField(max_length=2000)
    cooking_time = models.DurationField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title