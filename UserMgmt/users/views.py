from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    """Viewset for CRUD operations on User model"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
