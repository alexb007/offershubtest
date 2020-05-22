from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel


class Workspace(BaseModel):
    gid = models.CharField(
        max_length=32,
        unique=True,
        null=True,
        editable=False,
        verbose_name=_("GID"),
    )
    name = models.CharField(
        max_length=512,
        verbose_name=_("Название задачи")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Рабочее пространство')
        verbose_name_plural = _('Рабочие пространства')
