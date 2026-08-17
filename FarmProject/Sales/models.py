from django.db import models

from Farmers.models import Farmer
from Crops.models import crop


class Sale(models.Model):

    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name="sales"
    )

    Crop = models.ForeignKey(
        crop,
        on_delete=models.CASCADE,
        related_name="sales"
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    price_per_unit = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    sale_date = models.DateField()

    buyer = models.CharField(
        max_length=100
    )

    def __str__(self):
        return f"{self.crop} - {self.total_amount}"
