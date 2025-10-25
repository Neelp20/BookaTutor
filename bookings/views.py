# from django.shortcuts import render

# Create your views here.


# def bookings(request):
#     """ A view to return the bookings page """

#     return render(request, 'bookings/bookings.html')

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic import DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Booking, TimeSlot
from .forms import BookingForm


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
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        tutor_id = self.request.GET.get('tutor')
        slot_id = self.request.GET.get('slot')
        if tutor_id:
            initial['tutor'] = tutor_id
        if slot_id:
            initial['timeslot'] = slot_id
        return initial

    def form_valid(self, form):
        print("DEBUG POST DATA:", form.data)
        form.instance.student = self.request.user
        return super().form_valid(form)


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


class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = 'bookings/confirm_delete_booking.html'
    success_url = reverse_lazy('manage-bookings')

    def test_func(self):
        return self.get_object().student == self.request.user


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
