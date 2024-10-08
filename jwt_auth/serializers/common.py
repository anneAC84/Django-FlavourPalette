from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    #tell Django that certain fields should only be deserialized and not serialized
    #If we assign write_only=True to a field, it will only be used when creating and will not be used when retrieving
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        # custom validation here
        password =data.pop('password')
        password_confirmation = data.pop('password_confirmation')

       # check passwords match, invalidate if not
        if password != password_confirmation:
            raise serializers.ValidationError({'password_confimation': 'Passwords do not match.'})

        # validate password
        password_validation.validate_password(password=password)

        #add password back to the data dict, this time hashed
        data['password'] = make_password(password)


        # return data after validation
        return data
    

    def validate_email(self, value):
        # Check if email is already taken
        if User.objects.filter(email=value).exists():
            print("Validation Error: Email already exists.")
            raise serializers.ValidationError("User with this email already exists.")
        return value
    
    
    def validate_username(self, value):
        # Check if username is already taken
        if User.objects.filter(username=value).exists():
            print("Validation Error: Username already exists.")
            raise serializers.ValidationError("A user with that username already exists.")
        return value
           

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'profile_image','password', 'password_confirmation')