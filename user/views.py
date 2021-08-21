from .serializers import RegisterSerializer
from .models import UserModel
from django.shortcuts import render
from rest_framework import generics, permissions
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        return serializer.save()
