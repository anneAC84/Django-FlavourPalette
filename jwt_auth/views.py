from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers.common import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers.tokens import CustomObtainPairSerializer

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer

#signUp view
class SignUpView(APIView):

    # Create user
    def post(self, request):
        try:
          user_to_create = UserSerializer(data=request.data)
          if user_to_create.is_valid():
             user_to_create.save()
             return Response({'message': 'sign up successful.'}, 201)
          return Response(user_to_create.errors, 400)
        except Exception as e:
            print ('Error', e)
            return Response('An error occured',500)
    


