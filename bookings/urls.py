# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.Booking, name='bookings')
    
# ]

from django.urls import path
from .views import (
    BookingListView, PastBookingListView, BookingCreateView,
    BookingUpdateView, BookingDeleteView, AdminBookingListView,
    BookingCalendarView
)

urlpatterns = [
    path('', BookingCreateView.as_view(), name='bookings'),
    path('manage/', BookingListView.as_view(), name='manage-bookings'),
    path('past/', PastBookingListView.as_view(), name='past-bookings'),
    path('edit/<int:pk>/', BookingUpdateView.as_view(), name='edit-booking'),
    path('delete/<int:pk>/', BookingDeleteView.as_view(), name='delete-booking'),
    path('admin/manage/', AdminBookingListView.as_view(), name='admin-manage-bookings'),
    path('calendar/', BookingCalendarView.as_view(), name='booking-calendar'),
]

