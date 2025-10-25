from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta, time
from django.utils import timezone
from .models import Booking, TimeSlot
from tutors.models import Tutor


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('tutor', 'date', 'start_time', 'end_time')
    list_filter = ('tutor', 'date')
    search_fields = ('tutor__user__username', 'tutor__user__first_name', 'tutor__user__last_name')
    actions = ['generate_future_slots', 'delete_past_slots']

    def generate_future_slots(self, request, queryset):
        """Admin action: generate 3 months of slots for all tutors"""
        start_date = datetime.now().date() + timedelta(days=1)
        end_date = start_date + timedelta(days=90)
        created_count = 0

        for tutor in Tutor.objects.all():
            if tutor.user.is_superuser:
                continue  # Skip admins

            for i in range((end_date - start_date).days):
                date = start_date + timedelta(days=i)
                for start, end in [(time(10, 0), time(11, 0)), (time(14, 0), time(15, 0))]:
                    _, created = TimeSlot.objects.get_or_create(
                        tutor=tutor,
                        date=date,
                        start_time=start,
                        end_time=end
                    )
                    if created:
                        created_count += 1

        messages.success(request, f"✅ {created_count} time slots created for all tutors (next 3 months).")

    generate_future_slots.short_description = "📅 Generate Future Time Slots (Next 3 Months)"

    def delete_past_slots(self, request, queryset):
        """Admin action: delete all time slots before today (no selection required)"""
        today = timezone.now().date()
        deleted_count, _ = TimeSlot.objects.filter(date__lt=today).delete()

        if deleted_count:
            self.message_user(request, f"🧹 {deleted_count} old time slots deleted successfully.")
        else:
            self.message_user(request, "🧹 No old time slots found to delete.")

        return HttpResponseRedirect(request.get_full_path())

    delete_past_slots.short_description = "🧹 Delete Old Time Slots (Before Today)"

    # ✅ This override lets us run the delete action without selecting any checkboxes
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)
        if request.method == 'POST' and 'action' in request.POST:
            action = request.POST.get('action')
            if action == 'delete_past_slots':
                return self.delete_past_slots(request, queryset=None)
        return response


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('student', 'tutor', 'timeslot', 'subject', 'created_at')
    list_filter = ('tutor', 'timeslot__date')
    search_fields = (
        'student__username',
        'student__first_name',
        'student__last_name',
        'tutor__user__username'
    )





