from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


from .models import *
from .serializers import *
from .pagination import *
from .filters import *

# Create your views here.


# Category views
class CategoryViews(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    #Pagination:
    pagination_class = PaginationOfTen
    
    #Filtering:
    filter_backends = [SearchFilter]
    search_fields = ['name']
    
    #Persmission
    permission_classes = [IsAdminUser]
    
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
    
    #Pagination:
    pagination_class = PaginationOfTen
    
    #Filtering:
    filter_backends = [SearchFilter]
    search_fields = ['name']
    
    #Persmission
    permission_classes = [IsAdminUser]

    
    
    
# Post views
class PostViews(ModelViewSet):
    queryset = Post.objects.select_related('category').all()          # 'select_related('field_name')' join the foreign key table to optimize query on the db
    serializer_class = PostSerializer
    
    #Pagination:
    pagination_class = PaginationOfFifty
    
    #Filtering:
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_class = PostFilter
    
    #Persmission
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    
# Comment views
class CommentViews(ModelViewSet):
    queryset = Comment.objects.select_related('post').all()     # 'select_related() is used for optimization
    serializer_class = CommentSerializer
    
    #Pagination:
    pagination_class = PaginationOfTwenty
    
    #Filtering:
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['comment']
    filterset_class = CommentFilter
    
    #Persmission
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
# PostTag views
class PostTagViews(ModelViewSet):
    queryset = PostTag.objects.all()
    serializer_class = PostTagSerializer
    
    #Pagination:
    pagination_class = PaginationOfTen
    
    #Filtering:
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostTagFilter
    
    #Persmission
    permission_classes = [IsAuthenticated]


# User views
class UserViews(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    #Pagination: 
    pagination_class = PaginationOfTen
    
    #Filtering: 
    filter_backends = [SearchFilter]
    search_fields = ['username']
    
    #Persmission
    permission_classes = [IsAuthenticated]
    