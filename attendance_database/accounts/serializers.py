from rest_framework import serializers
from .models import CustomUser
from django.core import exceptions as django_exceptions
from django.contrib.auth.password_validation import validate_password

class CustomUserSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "role",
            "sex",
            "birthday",
            "age",
            "date_joined",
        ]
        read_only_fields = ["id", "full_name", "age", "date_joined"]

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    birthday = serializers.DateField(format="%Y-%m-%d", required=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "sex",
            "birthday",
        ]
