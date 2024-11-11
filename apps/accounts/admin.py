from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User  # Ensure the import statement is correct

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'gender', 'second_name', 'email', 'avatar', 'phone_number')

