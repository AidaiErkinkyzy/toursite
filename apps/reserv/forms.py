
from .models import *
from django import forms




class ResetForm(forms.ModelForm):
    date= forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2025)),
        required=False)


    class Meta:
        model = Reserv
        fields = ['name', 'phone_number', 'number_of_guests', 'check_in_date', 'destination']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_guests': forms.Select(attrs={'class': 'form-control-file'}),
            'check_in_date': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.Select(attrs={'class': 'form-control'}),
        }