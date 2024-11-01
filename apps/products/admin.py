from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Categories, Products, ProductsImage

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'slug', 'description', 'population', 'territory', 'continent')  # Отображение полей в админке

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'slug', 'description', 'price', 'quantity', 'is_active', 'category')


@admin.register(ProductsImage)
class ProductsImageAdmin(admin.ModelAdmin):
     list_display = ('id', 'product', 'image')
