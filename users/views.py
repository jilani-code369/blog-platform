from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .serializers import *



# Registeration API
@extend_schema(tags=['Register API'], request = RegisterSerializer, responses = RegisterSerializer)
class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()                                            # serializer.save() return the model object
        token, created = Token.objects.get_or_create(user = user)           # in 'user = user', the left side is a keyworked argument and right side user is the user model object/instance as its value 
        
        return Response({
            "message":"Registeration successful. ",
            "detail": serializer.data,
            "token":token.key
            
        }, status = status.HTTP_201_CREATED)
        
        

 # Login API:
@extend_schema(tags=['Login API'], request = LoginSerializer, responses = LoginSerializer)
class LoginAPI(APIView):
    def post(self, request):
       serializer = LoginSerializer(data = request.data)
       serializer.is_valid(raise_exception = True)
    
       user = serializer.validated_data['user']                                 # get the user object from the validated_data
       token, created = Token.objects.get_or_create(user = user)                # pass the user object to create token 
       
       return Response({
           "message":"Login successful",
           "detail":{
               "token":token.key
           }
       })



# Logout API
@extend_schema(tags=['Logout API'])
class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()                                   # delete the token from the db

        return Response({
            "message": "Logout successful"
        }, status=status.HTTP_200_OK)


