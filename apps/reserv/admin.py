from django.contrib import admin

# Register your models here.
from .models import Reserv
@admin.register(Reserv)
class ReservAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'phone_number', 'number_of_guests', 'check_in_date', 'destination')
