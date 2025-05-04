from rest_framework import serializers
from .models import Payment
from bookings.serializers import BookingSerializer

class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(),
        source='booking',
        write_only=True
    )
    
    class Meta:
        model = Payment
        fields = ['id', 'booking', 'booking_id', 'payment_method_id', 
                 'amount', 'status', 'created_at']