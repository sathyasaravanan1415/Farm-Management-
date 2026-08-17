from rest_framework import serializers
from .models import Sale
from datetime import date 

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sale
        fields="__all__"
        read_only_fields = ["total_amount"]

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Quantity must be greater than 0."
            )
        return value

    def validate_price_per_unit(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price per unit must be greater than 0."
            )
        return value

    def validate_sale_date(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                "Sale date cannot be in the future."
            )
        return value

    def validate_buyer(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                "Buyer name must be at least 2 characters."
            )
        return value

    def create(self, validated_data):
        quantity = validated_data["quantity"]
        price = validated_data["price_per_unit"]

        validated_data["total_amount"] = quantity * price

        return Sale.objects.create(**validated_data)

    def update(self, instance, validated_data):
        quantity = validated_data.get(
            "quantity", instance.quantity
        )
        price = validated_data.get(
            "price_per_unit", instance.price_per_unit
        )

        validated_data["total_amount"] = quantity * price

        return super().update(instance, validated_data)