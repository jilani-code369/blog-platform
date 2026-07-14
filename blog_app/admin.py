from django.contrib import admin

from .models import *

# Register your models here.


# Category admin customization 
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']           # tell which columns to display in admin panel
    list_display_links = ['id', 'name']     # tell which column should open edit option on clicking 
    
    list_filter = ['name']                  # tell which fields should be used for filtering
    search_fields = ['name']                # tell which fields should be used for searching
    list_per_page = 10                      # tell how many data/rows should appear per page
    
    
    
# Tag admin customization 
@admin.register(Tag)
class CategoryTag(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 10 
    



# Post admin customization 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id',  'title', 'author','description', 'category', 'tags', 'published_date', 'updated_at']
    list_display_links = ['id', 'author', 'title']
    
    list_filter = ['author', 'category', 'tags']
    search_fields = ['title', 'author__username']
    list_per_page = 10 
    



# Comment admin customization 
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'comment', 'parent_comment', 'commented_date', 'updated_at']
    list_display_links = ['id', 'user', 'post']
    
    list_filter = ['user']
    search_fields = ['user__username', 'post__title']
    list_per_page = 10
    
    


# PostTagJunction admin customization 
@admin.register(PostTag)
class PosTagJunctiontAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'post']
    list_display_links = ['id', 'tag', 'post']
    
    list_filter = ['tag__name']
    search_fields = ['tag__name', 'post__name']
    list_per_page = 10
    

