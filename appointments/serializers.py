from rest_framework import serializers
from .models import AppointmentOption

class AppointmentOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentOption
        fields = ['id', 'name', 'slots', 'price']