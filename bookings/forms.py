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

        # Only future timeslots
        future_slots = TimeSlot.objects.filter(
            date__gte=timezone.now().date()).order_by('date', 'start_time'
                                                      )
        self.fields['timeslot'].queryset = future_slots

        # Tutors with at least one future slot
        available_tutor_ids = future_slots.values_list(
            'tutor_id', flat=True
            ).distinct()
        self.fields['tutor'].queryset = Tutor.objects.filter(
            id__in=available_tutor_ids
            )

        # Pre-filter timeslots if tutor is pre-selected
        initial = kwargs.get('initial', {})
        if 'tutor' in initial:
            self.fields['timeslot'].queryset = self.fields['timeslot'].queryset.filter(tutor=initial['tutor'])

    def clean(self):
        cleaned_data = super().clean()
        tutor = cleaned_data.get('tutor')
        timeslot = cleaned_data.get('timeslot')

        if not tutor or not timeslot:
            raise ValidationError("Please select a tutor and a time slot.")

        if timeslot.tutor != tutor:
            raise ValidationError(
                "Selected timeslot does not belong to this tutor."
                )

        slot_datetime = datetime.combine(timeslot.date, timeslot.start_time)
        now_plus_24h = datetime.now() + timedelta(hours=24)
        if slot_datetime < now_plus_24h:
            raise ValidationError(
                "Bookings must be made at least 24 hours in advance."
                )

        if Booking.objects.filter(tutor=tutor, timeslot=timeslot).exists():
            raise ValidationError(
                "This timeslot is already booked. Please choose another."
                )

        return cleaned_data
