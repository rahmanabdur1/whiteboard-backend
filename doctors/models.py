from django.db import models
from users.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.get_full_name()