from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import UserProfile # Ensure the import statement is correct

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'image', 'last_name', 'username', 'email')
