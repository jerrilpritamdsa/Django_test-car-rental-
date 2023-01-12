from django.db import models

# Create your models here.

class Vehicle(models.Model):
    CAR_TYPE =(
        ('SMALL_CAR','sm'),
        ('MINI_VAN','mv'),
        ('SUV','suv'),
    )
    
    FUEL_TYPE =(
        ('PETROL','p'),
        ('DISEL','d'),
        ('ELECTRIC','ev'),
    )
    TRANSMISSION =(
        ('PETROL','p'),
        ('DISEL','d'),
        ('ELECTRIC','ev'),
    )
    car_name = models.CharField(max_length=20)
    car_type= models.CharField(max_length=10, choices=CAR_TYPE)
    car_model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE)
    car_image = models.ImageField()
    price_per_hour = models.IntegerField()
    is_available = models.BooleanField()
    number_of_seats = models.CharField(max_length=2)
    transmission = models.BooleanField(max_length=20)
    milage = models.FloatField(max_length=20)
    air_bag = models.BooleanField() 
    location = models.CharField(max_length=100)
    free_cancellation = models.BooleanField()
    driver_aged = models.BooleanField()
    
    def __str__(self):
        return self.car_name