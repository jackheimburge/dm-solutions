from django.db import models

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


class Vehicle(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    msrp = models.DecimalField("MSRP", decimal_places=2, max_digits=10)
    color = models.CharField(max_length=30)
    notes = models.TextField(max_length=1000)
    engine = models.CharField(max_length=30)
    is_available = models.BooleanField(default=False)
    odometer = models.IntegerField()
    interior = models.CharField(max_length=40)
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

    def minimum_sale_price(self):
        if self.condition == 'new':
            return self.msrp * 0.9
        else:
            return self.msrp * 0.75

    def __str__(self):
        return f"{self.make} - {self.model}: ${self.msrp}"
