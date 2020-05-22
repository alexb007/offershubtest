from django.contrib.auth import user_logged_in
from django.dispatch import receiver

from ..tasks import populate_user_data

def model_post_save(sender, instance, **kwargs):
    if not instance.synced:
        instance.sync_remote()

@receiver(user_logged_in)
def user_logged(sender, user, request, **kwargs):
    populate_user_data.delay()
