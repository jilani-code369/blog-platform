from django.urls import path 
from rest_framework import routers
from debug_toolbar.toolbar import debug_toolbar_urls

from .views import *


router = routers.DefaultRouter()                # using routers to display api paths as clickable links in the browser
router.register('category', CategoryViews)
router.register('tag', TagViews)
router.register('post', PostViews)
router.register('comment', CommentViews)
router.register('post-tag', PostTagViews)
router.register('user', UserViews)


urlpatterns = [
    
] + router.urls  + debug_toolbar_urls()         # 'router.urls' registers router in urlpatterns