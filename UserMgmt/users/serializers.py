from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    def validate_first_name(self, value):
        """Ensure first letter of first_name is uppercase."""
        return value.capitalize()

    def validate_last_name(self, value):
        """Ensure first letter of last_name is uppercase."""
        return value.capitalize()

    class Meta:
        model = User
        exclude = ["user_permissions", "groups"]

    def validate_username(self, value):
        """Custom validation for username"""
        if "admin" in value.lower():
            raise serializers.ValidationError("Username cannot contain 'admin'.")
        return value

    def validate(self, data):
        """Custom validation for overall data"""
        if "email" in data and not (
            data["email"].endswith("@gmail.com") or data["email"].endswith("@yahoo.com")
        ):
            raise serializers.ValidationError(
                {"email": "Only gmail or yahoo emails are allowed."}
            )
        return data
