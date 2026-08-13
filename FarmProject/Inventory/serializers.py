from rest_framework import serializers
from .models import Inventory
from datetime import date


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = "__all__"

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                "Name must be at least 2 characters."
            )
        return value

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Quantity must be greater than 0."
            )
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0."
            )
        return value

    def validate_purchase_date(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                "Purchase date cannot be in the future."
            )
        return value