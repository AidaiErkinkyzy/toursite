
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms



class UserProfileForm(UserCreationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class': ' form-control', 'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    image = forms.ImageField(widget=forms.imageInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    last_name = forms.CharField(label='Last_name',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last_name'}))

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'image', ('last_name'), ('name')]




