from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe
from.serializers.common import RecipeSerializer

# Create your views here.

    
class RecipeListCreateView(APIView):
    #Index Route
    def get(self, request):
        recipes = Recipe.objects.all() 
        serialized_recipes = RecipeSerializer(recipes, many=True)
        print(serialized_recipes.data) 
        return Response(serialized_recipes.data)
    
    # Create Route
    def post(self, request):
        try:
           recipe_to_create = RecipeSerializer(data=request.data)
           if recipe_to_create.is_valid():  
              recipe_to_create.save()           
              return Response(recipe_to_create.data, 201)
           print('validation error:', recipe_to_create.errors)
           return Response(recipe_to_create.errors,400)
        except Exception as e:
            print ('Error', e)
            return Response('An error occured',500)
        
       
        

