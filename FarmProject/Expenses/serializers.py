from rest_framework import serializers
from .models import Expenses
from datetime import date

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expenses
        fields="__all__"

        def validate_amount(self, value):
          if value <= 0:
            raise serializers.ValidationError(
                "Amount must be greater than 0."
            )
          return value
 
    def validate_date(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                "Expense date cannot be in the future."
            )
        return value

    def validate_description(self, value):
        if value and len(value) < 3:
            raise serializers.ValidationError(
                "Description must be at least 3 characters."
            )
        return value