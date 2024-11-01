from django.urls import path
from .views import *

urlpatterns = [
    path('Reserv/', ReservView.as_view(), name='Reserv'),

]