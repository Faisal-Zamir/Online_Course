from django.db.models.signals import post_save
from django.dispatch import receiver
from . models import Profile
from users.models import User
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwarg):
    if created:
        Profile.objects.create(user = instance)