from django.contrib.auth import authenticate
from rest_framework import serializers

from authentication.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(
        max_length=255,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response
        fields = ('email', 'username', 'password', 'token')
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
