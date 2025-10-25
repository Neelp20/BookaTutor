from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic import DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Booking, TimeSlot
from .forms import BookingForm
from django.contrib import messages


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/manage_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(
            student=self.request.user,
            timeslot__date__gte=timezone.now().date()
            )


class PastBookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/past_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(
            student=self.request.user, 
            timeslot__date__lt=timezone.now().date()
            )


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/bookings.html'
    success_url = reverse_lazy('manage-bookings')

    def get_form_kwargs(self):
        """Pass the current user to the form for filtering available tutors and timeslots"""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):
        """Pre-fill tutor and slot if passed in URL"""
        initial = super().get_initial()
        tutor_id = self.request.GET.get('tutor')
        slot_id = self.request.GET.get('slot')
        if tutor_id:
            initial['tutor'] = tutor_id
        if slot_id:
            initial['timeslot'] = slot_id
        return initial

    def form_valid(self, form):
        """Assign student and show success message"""
        form.instance.student = self.request.user
        messages.success(self.request, "✅ Booking created successfully!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(
            self.request,
            "❌ There was an error creating your booking. Please try again.")
        return super().form_invalid(form)


class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/bookings.html'
    success_url = reverse_lazy('manage-bookings')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def test_func(self):
        return self.get_object().student == self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, "✅ Booking updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "❌ Could not update booking. Please check the form and try again.")
        return super().form_invalid(form)


class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = 'bookings/confirm_delete_booking.html'
    success_url = reverse_lazy('manage-bookings')

    def test_func(self):
        return self.get_object().student == self.request.user
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "🗑️ Booking deleted successfully.")
        return super().delete(request, *args, **kwargs)


class AdminBookingListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Booking
    template_name = 'bookings/admin_manage_bookings.html'
    context_object_name = 'bookings'

    def test_func(self):
        return self.request.user.is_superuser


class BookingCalendarView(LoginRequiredMixin, TemplateView):
    template_name = 'bookings/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timeslots = TimeSlot.objects.filter(
            date__gte=timezone.now().date()).order_by('date', 'start_time'
                                                      )
        events = []
        for slot in timeslots:
            events.append({
                'title': f"{slot.tutor.user.get_full_name()}",
                'start': f"{slot.date}T{slot.start_time}",
                'end': f"{slot.date}T{slot.end_time}",
                'url': f"/bookings/?tutor={slot.tutor.id}&slot={slot.id}",
                'color': '#28a745' if slot.bookings.count() == 0 else '#dc3545',
            })
        context['events'] = events
        return context
