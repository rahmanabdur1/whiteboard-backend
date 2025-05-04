from django.db import models
from users.models import User
from appointments.models import AppointmentOption

class Booking(models.Model):
    appointment_date = models.DateField()
    treatment = models.ForeignKey(AppointmentOption, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('appointment_date', 'patient', 'treatment')
    
    def __str__(self):
        return f"{self.patient.email} - {self.treatment.name}"