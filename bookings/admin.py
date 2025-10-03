from django.contrib import admin
from .models import Booking, TimeSlot

# Register your models here.


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('tutor', 'date', 'start_time', 'end_time')
    list_filter = ('tutor', 'date')
    search_fields = ('tutor__user__username', 'tutor__user__first_name', 'tutor__user__last_name')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('student', 'tutor', 'timeslot', 'subject', 'created_at')
    list_filter = ('tutor', 'timeslot__date')
    search_fields = ('student__username', 'student__first_name', 'student__last_name', 'tutor__user__username')
