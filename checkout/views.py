from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.views import View
from django.contrib import messages
from bookings.models import Booking
from .models import Payment
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    """Create a Stripe Checkout Session for a booking"""

    def post(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(
            Booking, id=booking_id, student=request.user)
        amount = float(booking.tutor.hourly_rate)

        try:
            # Create Stripe Checkout Session
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'gbp',
                            'product_data': {
                                'name': f'Tutoring session with {booking.tutor.user.get_full_name()}',
                            },
                            'unit_amount': int(amount * 100),  # convert £ to pence
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=request.build_absolute_uri('/checkout/success/'),
                cancel_url=request.build_absolute_uri('/checkout/cancel/'),
            )

            # Create Payment record
            Payment.objects.create(
                booking=booking,
                stripe_payment_intent=checkout_session['id'],
                amount=amount,
                paid=False
            )

            return redirect(checkout_session.url, code=303)

        except Exception as e:
            messages.error(request, f"Error creating checkout session: {e}")
            return redirect('manage-bookings')
