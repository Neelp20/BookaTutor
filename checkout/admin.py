from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'booking', 'amount', 'paid', 'created_at')
    list_filter = (
        'paid', 'created_at')
    search_fields = (
        'booking__student__username', 'booking__tutor__user__username')
