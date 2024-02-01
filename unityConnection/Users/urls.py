from django.contrib import admin
from django.urls import path
from .views import UserAPIView

urlpatternsUsers = [
    path('api/UserList/', UserAPIView.as_view(), name="UserList"),
]
