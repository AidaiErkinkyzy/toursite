from django.urls import path
from .views import *

urlpatterns = [
    path('Reserv/', ResetView.as_view(), name='Reserv'),

]