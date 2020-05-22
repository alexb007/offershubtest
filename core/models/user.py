from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel
from core.tasks import sync_model


class AsanaUser(BaseModel):
    gid = models.CharField(
        max_length=32,
        unique=True,
        null=True,
        editable=False,
        verbose_name=_("GID"),
    )
    name = models.CharField(
        max_length=512,
        verbose_name=_("Имя пользователя")
    )

    def sync_remote(self):
        return sync_model.delay(self.id, 'User')

    @property
    def resource_type(self):
        return 'user'

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return self.name
