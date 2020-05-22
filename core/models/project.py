from django.db import models
from django.utils.translation import gettext_lazy as _

from core import api
from core.models.base import BaseModel
from core.tasks import sync_model


class Project(BaseModel):
    gid = models.CharField(
        max_length=128,  # TODO узнать максимальную длину для поля gid в asana
        unique=True,
        null=True,
        editable=False,
        verbose_name=_("GID"),
    )
    name = models.CharField(
        max_length=512,
        verbose_name=_("Название проекта")
    )

    @property
    def resource_type(self):
        return 'project'

    def remote_create(self):
        return sync_model.delay(self.id, 'Project')

    def sync_remote(self):
        return sync_model.delay(self.id, 'Project')

    class Meta:
        verbose_name = _("Проект")
        verbose_name_plural = _("Проекты")

    def __str__(self):
        return self.name
