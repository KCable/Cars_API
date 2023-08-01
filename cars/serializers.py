from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields =['id', 'make', 'model', 'year', 'price', 'date_added', 'dealership']
        depth = 1
        