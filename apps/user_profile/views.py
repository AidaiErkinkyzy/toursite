from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import UserProfile



class UserProfile(ListView):
    model = UserProfile
    template_name = 'pages/user_profile.html'
    context_object_name = 'user_profile'