from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *

# Create your views here.


# Category views
class CategoryViews(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# Tag views
class TagViews(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    
    
# Post views
class PostViews(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
    
# Comment views
class CommentViews(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    
    
# PostTag views
class PostTagViews(ModelViewSet):
    queryset = PostTag.objects.all()
    serializer_class = PostTagSerializer
    


# User views
class UserViews(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer