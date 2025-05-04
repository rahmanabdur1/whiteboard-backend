from django.urls import path
from .views import CreatePaymentIntent, PaymentList

urlpatterns = [
    path('create-payment-intent/', CreatePaymentIntent.as_view(), name='create-payment-intent'),
    path('', PaymentList.as_view(), name='payment-list'),
]