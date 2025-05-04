from rest_framework import generics, status
from rest_framework.response import Response
from .models import AppointmentOption
from .serializers import AppointmentOptionSerializer
from bookings.models import Booking
from django.db.models import Q
from datetime import date

class AppointmentOptionList(generics.ListAPIView):
    serializer_class = AppointmentOptionSerializer
    
    def get_queryset(self):
        queryset = AppointmentOption.objects.all()
        date_param = self.request.query_params.get('date')
        
        if date_param:
            # Get booked slots for the date
            booked_slots = Booking.objects.filter(
                appointment_date=date_param
            ).values_list('treatment', 'slot')
            
            # Create a dictionary of booked slots by treatment
            booked_dict = {}
            for treatment_id, slot in booked_slots:
                if treatment_id not in booked_dict:
                    booked_dict[treatment_id] = []
                booked_dict[treatment_id].append(slot)
            
            # Filter out booked slots
            for option in queryset:
                if option.id in booked_dict:
                    option.slots = [slot for slot in option.slots if slot not in booked_dict[option.id]]
        
        return queryset

class AppointmentSpecialtyList(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        specialties = AppointmentOption.objects.values('name').distinct()
        return Response([{'name': item['name']} for item in specialties])