from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from pages.models import Page


@receiver(post_save, sender=User)
def create_page(sender, **kwargs):
    instance = kwargs.get('instance')

    if instance:
        Page.objects.get_or_create(user=instance)
