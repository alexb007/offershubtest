from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    synced = models.BooleanField(
        default=False,
        verbose_name=_('Синхронизировано')
    )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, synced=False):
        self.synced = synced
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True
