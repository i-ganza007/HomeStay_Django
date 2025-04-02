from rest_framework import serializers
from .models import User
from rest_framework.permissions import AllowAny



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 
        permissions = [AllowAny]