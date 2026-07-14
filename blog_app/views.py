from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from .pagination import *

# Create your views here.


# Category views
class CategoryViews(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PaginationOfTen      #pagination 
    
    #override 'destroy()' method to handle deletion of protected relationship
    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        if PostTag.objects.filter(post__category = category).exists():
            return Response({"error":"Protected! Category cannot be deleted. Related to PostTag model."}, status = status.HTTP_400_BAD_REQUEST)
        return Response({"detail":"Category deleted successfully."}, status = status.HTTP_204_NO_CONTENT)


# Tag views
class TagViews(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = PaginationOfTen
    
    
# Post views
class PostViews(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PaginationOfFifty
    
    
    
# Comment views
class CommentViews(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PaginationOfTwenty
    
    
    
# PostTag views
class PostTagViews(ModelViewSet):
    queryset = PostTag.objects.all()
    serializer_class = PostTagSerializer
    pagination_class = PaginationOfTen
    


# User views
class UserViews(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PaginationOfTen