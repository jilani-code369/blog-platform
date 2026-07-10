from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA


from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(UA):         # 'UserAdmin' is used bec it hash the password unlike 'MOdelAdmin'
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'role', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined']
    list_display_links = ['id', 'username']
    list_editable = ['is_staff', 'is_active', 'is_superuser']  # tell which column you want to edit from the admin panel only without opening the editing page
    
    list_filter = ['is_staff', 'is_active', 'is_superuser']
    search_fields = ['username', 'first_name', 'last_name']
    list_per_page = 10

    fieldsets = (                                       # to customize fields for creating new user 
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email", "role")}),  # here "role" is added as a new field here 
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    