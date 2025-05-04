from django.urls import path
from .views import ContactCreate

urlpatterns = [
    path('', ContactCreate.as_view(), name='contact-create'),
]