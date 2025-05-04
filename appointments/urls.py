from django.urls import path
from .views import AppointmentOptionList, AppointmentSpecialtyList

urlpatterns = [
    path('', AppointmentOptionList.as_view(), name='appointment-option-list'),
    path('specialties/', AppointmentSpecialtyList.as_view(), name='appointment-specialty-list'),
]