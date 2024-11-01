from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Reserv

class ReservView(ListView):
    model = Reserv
    template_name = 'pages/reservation.html'
    context_object_name = 'reservation'