from django.shortcuts import render
from django.views.generic import TemplateView



class HomeView(TemplateView):
    template_name = 'pages/home.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class ReservationView(TemplateView):
    template_name = 'pages/reservation.html'


class User_ProfileView(TemplateView):
    template_name = 'pages/user_profile.html'


class ProductsView(TemplateView):
    template_name = 'pages/products.html'

