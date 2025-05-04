from rest_framework import serializers
from .models import Booking
from appointments.serializers import AppointmentOptionSerializer

class BookingSerializer(serializers.ModelSerializer):
    treatment = AppointmentOptionSerializer(read_only=True)
    treatment_id = serializers.PrimaryKeyRelatedField(
        queryset=AppointmentOption.objects.all(),
        source='treatment',
        write_only=True
    )
    
    class Meta:
        model = Booking
        fields = ['id', 'appointment_date', 'treatment', 'treatment_id', 
                 'slot', 'phone', 'price', 'created_at']