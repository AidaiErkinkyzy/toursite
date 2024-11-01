from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Products, ProductsImage, Categories

class CategoriesView(ListView):
    model = Categories
    template_name = 'pages/home.html'
    context_object_name = 'categories'

class ProductsImageView(ListView):
    model = ProductsImage
    template_name = 'pages/about.html'
    context_object_name = 'images'

class ProductsView(ListView):
    model = Products
    template_name = 'pages/about.html'
    context_object_name = 'products'
    queryset = Products.objects.all()
