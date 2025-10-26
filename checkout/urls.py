from django.urls import path
from .views import (
    CreateCheckoutSessionView, PaymentSuccessView, PaymentCancelView
)

urlpatterns = [
    path(
        'create/<int:booking_id>/', CreateCheckoutSessionView.as_view(),
        name='create-checkout-session'),
    path('success/', PaymentSuccessView.as_view(
        template_name='checkout/payment_success.html'),
          name='payment_success'),
    path('cancel/', PaymentCancelView.as_view(
        template_name='checkout/payment_cancel.html'), name='payment_cancel'),
]
