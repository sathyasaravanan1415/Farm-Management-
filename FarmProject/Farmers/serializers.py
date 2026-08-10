from rest_framework import serializers
from .models import Farmer

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Farmer
        fields="__all__"

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Name must be at least 3 characters."
            )
        return value

    def validate_phone(self, value):
        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must contain exactly 10 digits."
            )
        return value

    def validate_email(self, value):
        if Farmer.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "This email is already registered."
            )
        return value