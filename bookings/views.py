from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from users.models import User
from django.shortcuts import get_object_or_404

class BookingList(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Booking.objects.filter(patient=user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Check for existing booking
        existing_booking = Booking.objects.filter(
            patient=request.user,
            appointment_date=serializer.validated_data['appointment_date'],
            treatment=serializer.validated_data['treatment']
        ).exists()
        
        if existing_booking:
            return Response(
                {"acknowledged": False, "message": f"You already have a booking on {serializer.validated_data['appointment_date']}"},
                status=status.HTTP_200_OK
            )
        
        serializer.save(patient=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BookingDetail(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj