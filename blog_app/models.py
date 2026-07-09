from django.db import models
from django.contrib.auth import get_user_model  


# It fetches the active user of the project 
User = get_user_model()


# Category model 
class Category(models.Model):
    name = models.CharField(max_length = 20)


# Tag model 
class Tag(models.Model):
    name =  models.CharField(max_length = 20)


# Post model 
class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title =  models.CharField(max_length = 30)
    description = models.TextField()
    category =  models.ForeignKey(Category, on_delete = models.PROTECT)
    tags = author = models.ForeignKey(Tag, on_delete = models.SET_NULL, blank=True, null = True)
    creaed_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)



# Comment model 
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.TextField()
    parent_commnet = models.ForeignKey('self', on_delete = models.CASCADE)    # 'self' is used to point to own class for nesting comments   
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    

# Tag-Post-Junction model                                # for many-to-many relation with tags and post
class Tag_Post_Junction(models.Model):                         
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCASE)
    
