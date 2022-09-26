from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializers
from .models import Hero

# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializers
