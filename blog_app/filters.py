from django_filters import FilterSet

from .models import *


#Post filter: 
class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            "title" : ['icontains'],
            "author" : ['exact'],
            "category" : ['exact'],
            "tags" : ['exact'],
            "published_date" : ['gt']
            
        }
        

#Comment filter: 
class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            "post" : ['exact'],
            "user" : ['exact'],
            "comment" : ['icontains'],
            "commented_date" : ['gt']
            
        }



#PostTag Filer: 
class PostTagFilter(FilterSet):
    class Meta:
        model = PostTag
        fields = ['post', 'tag']
