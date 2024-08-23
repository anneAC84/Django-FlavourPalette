from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,AllowAny
from .models import Recipe
from.serializers.common import RecipeSerializer
from rest_framework.exceptions import PermissionDenied

# Create your views here.

    
class RecipeListCreateView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    #Index Route
    
    def get(self, request):
        recipes = Recipe.objects.all() 
        serialized_recipes = RecipeSerializer(recipes, many=True)
        print(serialized_recipes.data) 
        return Response(serialized_recipes.data)
    
    
    # Create Route
    def post(self, request):
        try:
           print('request user id->', request.user.id)
           request.data['owner'] = request.user.id
           recipe_to_create = RecipeSerializer(data=request.data)
           if recipe_to_create.is_valid():  
              recipe_to_create.save()           
              return Response(recipe_to_create.data, 201)
           print('validation error:', recipe_to_create.errors)
           return Response(recipe_to_create.errors,400)
        except Exception as e:
            print ('Error', e)
            return Response('An error occured',500)
        

  # path for this is /recipes/<int:pk>
class RecipeRetrieveUpdateDestroyView(APIView):
     permission_classes = [IsAuthenticated]
     #Retrieve
     def get(self, request,id):
        try:
             recipe = Recipe.objects.get(pk=id)
             serialized_recipe = RecipeSerializer(recipe)
             return Response(serialized_recipe.data)
        except Recipe.DoesNotExist as e:
             print(e)
             return Response({'message': 'Recipe not found'}, 404)
        except Exception as e:
             print(e.__class__.__name)
             return Response({'message': 'An unknown error has occured'}, 500)
       
            
     

      #Update
     def put(self, request,id):
         try:
              recipe_to_update = Recipe.objects.get(pk=id)
              if recipe_to_update.owner != request.user:
                  raise PermissionDenied()

              serialized_recipe = RecipeSerializer(recipe_to_update, data=request.data, partial=True)
              if serialized_recipe.is_valid():
                  serialized_recipe.save()
                  return Response(serialized_recipe.data)
              return Response(serialized_recipe.errors, 400)
         except PermissionDenied as e:
             print(e)
             return Response({'message': str(e)}, 403)
         except Recipe.DoesNotExist as e:
             print(e)
             return Response('Recipe not found.', 404)
         except Exception as e:
             print(e)
             return Response('An unknown error occured', 500)
         
     #Destroy
     def delete(self, request,id):
         try:
              recipe_to_delete = Recipe.objects.get(pk=id)

              if recipe_to_delete.owner != request.user:
                  raise PermissionDenied()
              recipe_to_delete.delete()
              return Response(status=204)
         except Recipe.DoesNotExist as e:
             print(e)
             return Response('Recipe not found.', 404)
         except Exception as e:
             print(e)
             return Response('An unknown error occured', 500)    

     
        
       
        

