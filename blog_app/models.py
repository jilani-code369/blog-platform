from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()     # to automatically fetch the active user of the project


# Category model 
class Category(models.Model):
    name = models.CharField(max_length = 20, unique=True)
    def __str__(self):          # it is a dunder function which displays string instead of objects in admin panel
        return (self.name)


# Tag model 
class Tag(models.Model):
    name =  models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return (self.name)
    

# Post model 
class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title =  models.CharField(max_length = 30)
    description = models.TextField()
    category =  models.ForeignKey(Category, on_delete = models.PROTECT)
    tags = models.ForeignKey(Tag, on_delete = models.SET_NULL, blank=True, null = True)
    published_date = models.DateTimeField(auto_now_add= True)       # 'auto_now_add'  set the current data/time only once, it cannot be changed
    updated_at = models.DateTimeField(auto_now = True)          # 'auto_now'  sets the current data/time but it changes after updating the table
    def __str__(self):
        return (self.title)



# Comment model 
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    user = models.ForeignKey(User, on_delete = models.CASCADE)  
    comment = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete = models.CASCADE, related_name = 'replies', blank=True, null = True)    # 'self' is used to point to own class for nesting comments   # we can also use 'Category' instead of 'self' but in quotes
    commented_date = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return (self.comment)
    
    

# PostTag junction model             # for many-to-many relation with post and tag
class PostTag(models.Model):                         
    tag = models.ForeignKey(Tag, on_delete = models.SET_NULL, null = True)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    
