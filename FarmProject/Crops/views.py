from django.shortcuts import render
from rest_framework import viewsets
from .models import crop
from .serializers import CropSerializer

class cropviewset(viewsets.ModelViewSet):
    queryset=crop.objects.all()
    serializer_class=CropSerializer
