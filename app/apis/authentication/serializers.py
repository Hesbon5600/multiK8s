from django.core.validators import MinValueValidator
from rest_framework import serializers
from .models import UserModel


class UserSentSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Payment objects."""
    id = serializers.CharField(read_only=True)

    class Meta:
        model = UserModel
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ('id', 'name', 'amount', 'status',)
