from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


# Category views

class LoginAPI(APIView):
    def post(self, request):
        my_username = request.data.get('username')
        my_password = request.data.get('password')
        if my_username is None or my_password is None:
            raise serializers.ValidationError({"detail":"Both fields are required."})
        
        valid_user = authenticate(username=my_username, password = my_password)
        print(valid_user)       # Output: user , because of the __str__() method which is by default present in the AbstractUser
        
        if valid_user:
            token, created = Token.objects.get_or_create(user = valid_user)
            return Response({
                "message":"Login successful!",
                "id":valid_user.id,
                 "username": valid_user.username,
                 "token": token.key}, status = status.HTTP_200_OK)      # status is 200_OK not 201_CREATED bec its main function is login(authentication) not creation
            return Response({"error":"Incorrect username or password!"}, status = status.HTTP_401_UNAUTHORIZED)
        
        
        
        
        
         
#Logic of login:

# 1- start
# 2- get username and password from request
# 3- check if the username or password field is non-empty
#     if empty, raise error by saying "both fields are required"
#   
#
# 4- check if the provided username and passsword is correct/match with the db record or not 
#     a- if correct:
#         i- create/get the token of that user
#         ii- display/return success message with infos (user id, username, email, token)
#
#     b- display/return "Incorrect username or password" 
#
# 6- end
