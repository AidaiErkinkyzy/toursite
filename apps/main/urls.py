from django.urls import path
from . views import *
# from ..accounts.views import RegisterView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('user_profile/', User_ProfileView.as_view(), name='user_profile'),
    path('products/', ProductsView.as_view(), name='products'),

]