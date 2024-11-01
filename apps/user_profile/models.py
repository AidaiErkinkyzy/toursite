from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Model
from django.urls import reverse



class UserProfile(models.Model):
    image = models.ImageField(upload_to='profile_images', blank=True, null=True, verbose_name='фото')
    name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    username = models.CharField(max_length=150, unique=True, verbose_name='имя пользователя')
    email = models.EmailField(max_length=254, unique=True, verbose_name='емайл')

    class Meta:
        db_table = 'user_profile'
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователя'

    def __str__(self):
        return self.username
