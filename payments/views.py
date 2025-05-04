import stripe
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from bookings.models import Booking
from django.conf import settings
from django.shortcuts import get_object_or_404

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreatePaymentIntent(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try:
            booking_id = request.data.get('booking_id')
            booking = get_object_or_404(Booking, id=booking_id, patient=request.user)
            
            amount = int(booking.price * 100)  # Convert to cents
            
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                metadata={
                    'booking_id': str(booking.id),
                    'user_id': str(request.user.id)
                }
            )
            
            return Response({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

class PaymentList(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Payment.objects.filter(booking__patient=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        booking = serializer.validated_data['booking']
        if booking.patient != request.user:
            return Response(
                {'error': 'Not your booking'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)