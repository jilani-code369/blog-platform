from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()     # to fetch automatically the active user of the project


# Category model 
class Category(models.Model):
    name = models.CharField(max_length = 20)
    def __str__(self):          # dunder function to desplay string name instead of object in admin panel
        return (self.name)


# Tag model 
class Tag(models.Model):
    name =  models.CharField(max_length = 20)
    def __str__(self):
        return (self.name)
    

# Post model 
class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title =  models.CharField(max_length = 30)
    description = models.TextField()
    category =  models.ForeignKey(Category, on_delete = models.PROTECT)
    tags = models.ForeignKey(Tag, on_delete = models.SET_NULL, blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return (self.title)



# Comment model 
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    user = models.ForeignKey(User, on_delete = models.CASCADE)  
    comment = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete = models.CASCADE, related_name = 'replies', blank=True, null = True)    # 'self' is used to point to own class for nesting comments   # can also use 'Category' but in quotes
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return (self.comment)
    
    

# Tag-Post-Junction model             # for many-to-many relation with tags and post
class PosTagJunction(models.Model):                         
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    
