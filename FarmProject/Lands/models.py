from django.db import models
from Farmers.models import Farmer

class land(models.Model):
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE,related_name="lands")
    land_name = models.CharField(max_length=100)
    survey_number = models.CharField(max_length=50, unique=True)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    soil_type = models.CharField(max_length=100)
    irrigation_type = models.CharField(max_length=100)

    def __str__(self):
        return self.land_name



