from rest_framework import viewsets
from .models import FarmerProfile
from .serializers import FarmerProfileSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response


class FarmerProfileViewSet(viewsets.ModelViewSet):
    queryset=FarmerProfile.objects.all()
    serializer_class=FarmerProfileSerializer

class RegisterViewSet(viewsets.GenericViewSet):
    serializer_class=RegisterSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=201
        )


