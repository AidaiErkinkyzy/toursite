# Generated by Django 5.1.2 on 2024-11-01 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reserv',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
