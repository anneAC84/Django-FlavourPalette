from django.urls import path
from .views import SignUpView
from .views import CustomTokenObtainPairView


urlpatterns = [
    
    path('sign-up/', SignUpView.as_view()),
    path('sign-in/', CustomTokenObtainPairView.as_view(), name='sign-in')
]