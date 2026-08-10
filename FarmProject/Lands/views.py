from rest_framework import viewsets
from .models import land 
from .serializers import landSerializer 

class landViewSet(viewsets.ModelViewSet):
    queryset=land.objects.all()
    serializer_class=landSerializer
