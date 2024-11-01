from django.urls import path
from .views import *

urlpatterns = [
    path('UserProfile/', UserProfile.as_view(), name='UserProfile')

]