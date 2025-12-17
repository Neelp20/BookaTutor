from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update UserProfile whenever a User is created or saved.
    Ensures no 'User has no userprofile' errors.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Safely handle existing users that might not have a profile yet
        UserProfile.objects.get_or_create(user=instance)