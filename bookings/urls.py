from django.urls import path
from . import views

urlpatterns = [
    path(
        '', views.BookingCreateView.as_view(), name='bookings'),
    path(
        'manage/', views.BookingListView.as_view(), name='manage-bookings'),
    path(
        'edit/<int:pk>/', views.BookingUpdateView.as_view(), name='edit-booking'),
    path(
        'delete/<int:pk>/', views.BookingDeleteView.as_view(), name='delete-booking'),
    path(
        'past/', views.PastBookingListView.as_view(), name='past-bookings'),
    path(
        'admin/manage/', views.AdminBookingListView.as_view(), name='admin-manage-bookings'),
    path(
        'tutor/manage/', views.TutorBookingListView.as_view(), name='tutor-manage-bookings'),
    path(
        'confirm/<int:pk>/', views.ConfirmBookingView.as_view(), name='confirm-booking'),
    path(
        'reject/<int:pk>/', views.RejectBookingView.as_view(), name='reject-booking'),

]
