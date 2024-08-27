from rest_framework.serializers import ModelSerializer
from ..models import Recipe
from rest_framework import serializers
from jwt_auth.serializers.common import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RecipeSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    

    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user:
            validated_data['created_by'] = request.user
        return super().create(validated_data)