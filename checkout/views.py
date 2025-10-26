from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.conf import settings
from bookings.models import Booking
from .models import Payment
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    """Creates Stripe Checkout session for a booking"""

    def get(self, request, *args, **kwargs):
        booking_id = kwargs.get("booking_id")
        booking = get_object_or_404(Booking, id=booking_id)

        # ✅ Use defaults to ensure amount is set during creation
        payment, created = Payment.objects.get_or_create(
            booking=booking,
            defaults={'amount': booking.tutor.hourly_rate}
        )

        if not created and not payment.amount:
            payment.amount = booking.tutor.hourly_rate
            payment.save()

        # Create Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(booking.tutor.hourly_rate * 100),
                    'product_data': {
                        'name': f"Session with {booking.tutor.user.username}",
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/checkout/success/?session_id={CHECKOUT_SESSION_ID}'),
            cancel_url=request.build_absolute_uri('/checkout/cancel/'),
        )

        payment.stripe_checkout_id = checkout_session.id
        payment.save()

        return redirect(checkout_session.url)


class PaymentSuccessView(TemplateView):
    """Handles success after Stripe checkout"""
    template_name = "checkout/payment_success.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get("session_id")

        if session_id:
            try:
                payment = Payment.objects.get(stripe_checkout_id=session_id)
                payment.paid = True  # ✅ Correct field name
                payment.save()

                # Mark related booking as confirmed
                booking = payment.booking
                booking.confirmed = True
                booking.save()

                messages.success(
                    request, "✅ Payment successful! Your booking is confirmed."
                )
            except Payment.DoesNotExist:
                messages.error(request, "⚠️ Payment record not found.")
        else:
            messages.warning(request, "No session ID returned from Stripe.")

        return super().get(request, *args, **kwargs)


class PaymentCancelView(TemplateView):
    """Handles cancel from Stripe checkout"""
    template_name = "checkout/payment_cancel.html"

    def get(self, request, *args, **kwargs):
        messages.warning(
            request, "❌ Payment cancelled. You can try again anytime."
        )
        return super().get(request, *args, **kwargs)

