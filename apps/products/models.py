from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Model
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products_images', blank=True, null=True, verbose_name='Изображение')
    population = models.CharField(max_length=200, unique=True, blank=True, null=True, verbose_name='Популяция')
    territory = models.CharField(max_length=200, unique=True, blank=True, null=True, verbose_name='Территория')
    continent = models.CharField(max_length=100, blank=True, null=True, verbose_name='Континент')


    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'


class ProductsImage(models.Model):
    product = models.ForeignKey(Products, related_name='images', verbose_name='Продукты', on_delete=models.CASCADE)  # Измените 'image' на 'images'
    image = models.ImageField(verbose_name='Изображение', upload_to='dop_photo')

    class Meta:
        db_table = 'photos'
        verbose_name = 'Доп. фото'
        verbose_name_plural = 'Доп. фотки'

    def __str__(self):
        return str(self.image)





