from rest_framework import serializers
from .models import FarmerProfile

class FarmerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = FarmerProfile
        fields = "__all__"



# for creating the users securly in django and using default users module
#the pass word only belongs to the users doesn't go to the farmers profile
from django.contrib.auth.models import User
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )

        return user