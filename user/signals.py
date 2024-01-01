from django.dispatch import receiver
from .models import Customer
from django.db.models import signals
from django.contrib.auth.models import User

@receiver(signals.post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance).save()


@receiver(signals.pre_delete, sender=User)
def deletee_profie(sender, instance, **kwargs):
    instance.profile.delete()