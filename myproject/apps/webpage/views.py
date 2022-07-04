from django.shortcuts import render
from rest_framework import generics
from .models import Testimoni
from .serializers import TestiSerializer

# Create your views here.
class TestiList(generics.ListCreateAPIView):
    queryset = Testimoni.objects.all()
    serializer_class = TestiSerializer
    name = 'testimoni-list'