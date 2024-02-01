from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializer import UserSerializer

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
