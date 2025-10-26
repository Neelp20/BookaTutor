from django.db import models
from bookings.models import Booking


class Payment(models.Model):
    """Stores payment info for a Booking"""
    booking = models.OneToOneField(
        Booking, on_delete=models.CASCADE, related_name='payment'
    )
    stripe_payment_intent = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Stripe Payment Intent or Session ID"
    )
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Payment for {self.booking.student.username} → {self.booking.tutor.user.username} ({'Paid' if self.paid else 'Pending'})"
