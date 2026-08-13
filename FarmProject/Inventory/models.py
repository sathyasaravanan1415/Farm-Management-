from django.db import models

from django.db import models


class Inventory(models.Model):

    CATEGORY_CHOICES = [
        ("Seed", "Seed"),
        ("Fertilizer", "Fertilizer"),
        ("Pesticide", "Pesticide"),
        ("Equipment", "Equipment"),
        ("Other", "Other"),
    ]

    UNIT_CHOICES = [
        ("kg", "Kilogram"),
        ("liter", "Liter"),
        ("piece", "Piece"),
        ("bag", "Bag"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    unit = models.CharField(
        max_length=20,
        choices=UNIT_CHOICES
    )
    purchase_date = models.DateField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.name
