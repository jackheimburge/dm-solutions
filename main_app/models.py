from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

TRANSMISSIONS = (
    ('M', 'Manual'),
    ('A', 'Automatic'),
    ('D', 'Dual')
)
CONDITIONS = (
    ('N', 'New'),
    ('U', 'Used'),
    ('S', 'Salvage')
)
VEHICLE_TYPES = (
    ('C', 'Car'),
    ('P', 'Pickup'),
    ('B', 'Boat'),
    ('M', 'Motorcycle')
)

class Location(models.Model):
    city = models.CharField(max_length=30)
    state_code = models.CharField('State', max_length=2)
    zipcode = models.IntegerField('Zip Code')

    def __str__(self):
        return f'{self.city}, {self.state_code} {self.zipcode}'

    @property
    def combined(self):
        return f'{self.city}, {self.state_code} {self.zipcode}'

    def get_absolute_url(self):
        return reverse('vehicle_index')


class Vehicle(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    msrp = models.DecimalField("MSRP", decimal_places=2, max_digits=10)
    color = models.CharField(max_length=30)
    notes = models.TextField(max_length=1000)
    engine = models.CharField(max_length=30)
    is_available = models.BooleanField(default=True)
    odometer = models.IntegerField()
    interior = models.CharField(max_length=40)
    sold_for = models.DecimalField("Sold For", decimal_places=2, max_digits=10, blank=True, null=True)
    transmission = models.CharField(
        max_length=30,
        choices=TRANSMISSIONS,
        default=TRANSMISSIONS[1][0]
    )
    condition = models.CharField(
        max_length=30,
        choices=CONDITIONS,
        default=CONDITIONS[0][0]
    )
    vehicle_type = models.CharField(
        max_length=20,
        choices=VEHICLE_TYPES,
        default=VEHICLE_TYPES[0][0]
    )
    image = models.ImageField(upload_to="dms", blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('vehicle_detail', kwargs={'pk': self.id})

    def minimum_sale_price(self):
        if self.condition == 'new':
            return self.msrp * 0.9
        else:
            return self.msrp * 0.75

    def __str__(self):
        return f"{self.make} - {self.model}: ${self.msrp}"
