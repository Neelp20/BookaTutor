from django.contrib import admin
from .models import Tutor, Subject


admin.site.register(Subject)
admin.site.register(Tutor)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class TutorAdmin(admin.ModelAdmin):
    list_display = ('user', 'hourly_rate', 'years_of_experience')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    list_filter = ('subjects',)
    filter_horizontal = ('subjects',)
