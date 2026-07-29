from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import *

@receiver(post_save, sender = Post)
def notify(sender, instance, created, **kwargs):
    
    # print("Post created")
    
    send_mail(                                          # send email on post creation
        "Post created",
        "Your post has been created.",
        "settings.EMAIL_HOST_USER",
        ["dearjinni44@gmail.com", "maxhn6@gmail.com"]
    )
    
    
