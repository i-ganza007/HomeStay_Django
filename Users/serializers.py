from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        field = '__all__'
        