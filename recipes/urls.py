from django.urls import path
from .views import RecipeListCreateView


urlpatterns = [

    path('', RecipeListCreateView.as_view()), # /recipes
]
