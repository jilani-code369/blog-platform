
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


User = get_user_model()                                                         # it fetches active user model from the project


# Register Serializer:
class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only = True, validators = [validate_password])    # write_only = True don't send password in the browser but if you explicitely send it in response then it will be displayed there. validator validates using rules of setting.py
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)                       #point to be noted: 'create_user()' function is used to create a user bec it hash the password. normal 'create()' function doesn't hash the password. 
        return user



# Login Serializer: 

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)                           # they do field-level validation. they check if values are present in the field and do they have text/string type of data in them
    password = serializers.CharField(required = True)
    
    def validate(self, attr):                                                   # it does object-level validation. it check if the username and password with the database. 'attr' is a dictionary just like 'validated_data' which stores data that comes form the request. 
        username = attr.get('username')
        password = attr.get('password')
    
        user = authenticate(username = username, password = password)           # return the user object form the database if credential is correct 
        if not user:
            raise serializers.ValidationError({"detail":"Invalid username or password. "})

        attr['user'] = user                                                     # this line add a new key to the same dictionary
        # print(attr)                                                           # Output: {'username': 'mike', 'password': 'mike@12345', 'user': <User: mike>}
        
        return attr 
 
 
 
 