from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):
    """ Represents a subject that a tutor can teach"""
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        """ Order by name """
        ordering = ['name']

        def __str__(self):
            return self.name


class Tutor(models.Model):
    """Tutor profile linked to a user account"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tutor_profile')
    bio = models.TextField(blank=True, null=True)
    subjects = models.ManyToManyField(Subject, related_name='tutors')
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, help_text="GBP Rate")
    availability = models.TextField(
        help_text="Briefly describe availability (e.g., weekdays after 5pm, weekends)",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['user__username']

    def __str__(self):
        return self.user.get_full_name() or self.user.username