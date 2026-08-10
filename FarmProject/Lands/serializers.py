from rest_framework import serializers
from .models import land

class landSerializer(serializers.ModelSerializer):
    class Meta:
        model=land
        fields="__all__"