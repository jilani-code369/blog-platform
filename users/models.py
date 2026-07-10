from django.db import models

from django.contrib.auth.models import AbstractUser




# Custorm user model:
class User(AbstractUser):
    ROLE_CHOICES = [                
        ("author", "Author"), 
        ("reader", "Reader"), 
        ("admin", "Admin")
    ]
    role = models.CharField(max_length=20, choices = ROLE_CHOICES)   # role for role based access/system 





