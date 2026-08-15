from django.db import models

from django.db import models
from Farmers.models import Farmer


class Expenses(models.Model):

    CATEGORY_CHOICES = [
        ("Seeds", "Seeds"),
        ("Fertilizer", "Fertilizer"),
        ("Pesticide", "Pesticide"),
        ("Labor", "Labor"),
        ("Equipment", "Equipment"),
        ("Irrigation", "Irrigation"),
        ("Other", "Other"),
    ]

    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name="expenses"
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(
        blank=True
    )

    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount}"
