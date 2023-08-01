from django.db import models
from dealerships.models import Dealership

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    