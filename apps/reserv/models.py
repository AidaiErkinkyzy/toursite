from django.db import models

# Create your models here.

class Reserv(models.Model):
    GUEST_NUMBER_CHOICES = [
        (1, '1 Guest'),
        (2, '2 Guests'),
        (3, '3 Guests'),
    ]
    DESTINATION_CHOICES = [
    ('italy, roma', 'Italy, Roma'),
    ('france, paris', 'France, Paris'),
    ('england, london', 'England, London'),
    ('switzerland, lausanne', 'Switzerland, Lausanne'),
]


    name = models.CharField(max_length=100, verbose_name="Guest Name")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    number_of_guests = models.PositiveSmallIntegerField(choices=GUEST_NUMBER_CHOICES, verbose_name="Number of Guests")
    check_in_date = models.DateField(verbose_name="Check-in Date")
    destination = models.CharField(max_length=50, choices=DESTINATION_CHOICES, verbose_name="Destination")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.name