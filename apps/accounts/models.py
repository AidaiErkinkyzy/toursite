from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Менеджер пользователя
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# Основной класс пользователя
class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    second_name = models.CharField('Отчество', max_length=50, blank=True)
    email = models.EmailField('Электронная почта', unique=True)
    avatar = models.ImageField('Аватар', upload_to='avatars/', null=True, blank=True)
    phone_number = models.CharField('Номер телефона', max_length=15, blank=True)

    objects = UserManager()

    # Уникальные имена для обратных аксессоров
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_user_set',  # Уникальное имя
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_user_set',  # Уникальное имя
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'