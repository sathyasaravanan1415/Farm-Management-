from django.db import models
from Lands.models import land
class crop(models.Model):
    land=models.ForeignKey(land,on_delete=models.CASCADE,related_name="crops")
    crop_name=models.CharField(max_length=100)
    crop_type=models.CharField(max_length=100)
    season=models.CharField(max_length=100)
    sowing_date=models.DateField()
    harvest_date=models.DateField()
    quantity=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=50)



