from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from tutors.models import Tutor  # Tutor model in tutors app


class TimeSlot(models.Model):
    """Available slot for a tutor."""
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='time_slots')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('tutor', 'date', 'start_time', 'end_time')
        ordering = ['date', 'start_time']

    def __str__(self):
        return f"{self.tutor.user.get_full_name()} - {self.date} {self.start_time}-{self.end_time}"

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")
        if self.date < timezone.now().date():
            raise ValidationError("Time slot cannot be in the past.")


class Booking(models.Model):
    """Booking made by a student for a tutor's time slot."""
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='bookings')
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='bookings')
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)

    class Meta:
        unique_together = ('tutor', 'timeslot')
        ordering = ['timeslot__date', 'timeslot__start_time']

    def __str__(self):
        return f"{self.student.get_full_name()} -> {self.tutor.user.get_full_name()} on {self.timeslot.date} at {self.timeslot.start_time}"

    def clean(self):
        if self.timeslot.date < timezone.now().date():
            raise ValidationError("Cannot book a timeslot in the past.")
        if Booking.objects.filter(tutor=self.tutor, timeslot=self.timeslot).exclude(pk=self.pk).exists():
            raise ValidationError("This timeslot is already booked.")
