from django.urls import path
from .views import *

urlpatterns = [
    path('Categories/', CategoriesView.as_view(), name='Categories'),
    path('Products/', ProductsView.as_view(), name='Products'),
    path('ProductsImage/', ProductsImageView.as_view(), name='ProductsImage'),

]