from datetime import datetime, timedelta
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking, TimeSlot
from tutors.models import Tutor


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['tutor', 'timeslot', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(
                attrs={'placeholder': 'Any message for your tutor', 'rows': 3}
            ),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # ✅ Show all tutors
        self.fields['tutor'].queryset = Tutor.objects.all().order_by('user__username')

        # ✅ Show only future, unbooked timeslots
        available_slots = TimeSlot.objects.filter(
            date__gte=timezone.now().date(),
            bookings__isnull=True
        ).order_by('date', 'start_time')

        self.fields['timeslot'].queryset = available_slots

        # ✅ Determine selected tutor from data or initial
        tutor_id = None
        if self.data.get('tutor'):  # during POST or dropdown change
            tutor_id = self.data.get('tutor')
        elif 'tutor' in kwargs.get('initial', {}):  # from ?tutor= in URL
            tutor_id = kwargs['initial']['tutor']
        elif self.user and hasattr(self.user, 'tutor'):
            tutor_id = self.user.tutor.id  # fallback for logged-in tutor

        # ✅ Filter timeslots for that tutor
        if tutor_id:
            try:
                tutor_id = int(tutor_id)
                self.fields['timeslot'].queryset = available_slots.filter(tutor_id=tutor_id)
            except (ValueError, TypeError):
                pass

    def clean(self):
        cleaned_data = super().clean()
        tutor = cleaned_data.get('tutor')
        timeslot = cleaned_data.get('timeslot')

        if not tutor or not timeslot:
            raise ValidationError("Please select a tutor and a time slot.")

        # Timeslot must belong to the same tutor
        if timeslot.tutor != tutor:
            raise ValidationError("Selected timeslot does not belong to this tutor.")

        # Must be at least 24h in advance
        slot_datetime = datetime.combine(timeslot.date, timeslot.start_time)
        if slot_datetime < (datetime.now() + timedelta(hours=24)):
            raise ValidationError("Bookings must be made at least 24 hours in advance.")

        # No double booking
        if Booking.objects.filter(timeslot=timeslot).exists():
            raise ValidationError("This timeslot is already booked. Please choose another.")

        return cleaned_data




