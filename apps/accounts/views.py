from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'pages/register.html'
    success_url = reverse_lazy('login')


class LoginView(FormView):
    model = User
    form_class = LoginForm
    template_name = 'pages/login.html'
    success_url = '/'

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(username=username,
                            email=email, password=password)
        print(username)
        print(email)
        print(password)

        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('home')
            else:
                return HttpResponse('User have been banned')
        else:
            return HttpResponse('Wrong data or user is not found')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')

class ProfileView(FormView):
    def get(self, request):
        return HttpResponse('Profile Page')






