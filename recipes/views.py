from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe
from.serializers.common import RecipeSerializer

# Create your views here.

#Index Route
class RecipeListCreateView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all() 
        serialized_recipes = RecipeSerializer(recipes, many=True)
        print(serialized_recipes.data) 
        return Response(serialized_recipes.data)
