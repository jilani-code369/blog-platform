# serializers.py
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user
    
    
    


class LoginSerializer(serializers.Serializer):                                      # Using serializers.Serializer here bec. you don't need a model mapping for that. It just take two inputs (username, password) from the user and validate it. It doesn't do the CRUD operation to the model tha's why ModelSerializer is not used here. 
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

     
        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Incorrect username or password!")

    
        data['user'] = user
        return data