from rest_framework import serializers
from .models import crop
from datetime import date

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model=crop
        fields="__all__"

    def validate_name(self, value):
            if len(value) < 3:
                raise serializers.ValidationError(
                    "Name must be at least 3 characters."
                )
            return value

    def validate_quantity(self, value):
            if value <= 0:
               raise serializers.ValidationError(
                    "Quantity must be greater than 0.")
            return value

    def validate(self, data):
            if data["harvest_date"] < data["sowing_date"]:

                raise serializers.ValidationError(
                     "Harvest date must be after sowing date.")
        
            return data

    def validate(self,sowing_date):
         if sowing_date > date.today():
              raise serializers.ValidationError("Invalid sowing date")
         return sowing_date


    def validate(self,status):
         allowed=["Planned","Growing","Harvested"]
         if status not in allowed:
              raise serializers.ValidationError("Invalid crop status")
         return status
         


        