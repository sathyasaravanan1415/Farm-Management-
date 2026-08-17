from django.db import models
from django.contrib.auth.models import User
from Farmers.models import Farmer


class FarmerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    farmer = models.OneToOneField(
        Farmer,
        on_delete=models.CASCADE,
        related_name="user_profile"
    )

    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


