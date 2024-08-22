from django.urls import path
from .views import RecipeListCreateView, RecipeRetrieveUpdateDestroyView


urlpatterns = [

    path('', RecipeListCreateView.as_view()), # /recipes
    path('<int:id>/', RecipeRetrieveUpdateDestroyView.as_view()) # /recipes
    
]
