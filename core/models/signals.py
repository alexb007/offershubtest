from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Project


@receiver(post_save, sender=Project)
def save_project(sender, instance, created, **kwargs):
    if created:
        instance.remote_create()
    else:
        instance.sync_remote()
