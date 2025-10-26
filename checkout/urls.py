from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('success/', TemplateView.as_view(
        template_name='checkout/payment_success.html'),
          name='payment_success'),
    path('cancel/', TemplateView.as_view(
        template_name='checkout/payment_cancel.html'), name='payment_cancel'),
]
