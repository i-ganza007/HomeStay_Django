from .serializers import UserSerializer
from .models import User
from rest_framework import generics

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer