from rest_framework import serializers
from .models import Testimoni

class TestiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimoni
        fields = ("nama", "picture")