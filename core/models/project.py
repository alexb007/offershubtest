from django.db import models
from django.utils.translation import gettext_lazy as _

from core import api
from core.models.base import BaseModel
from core.tasks import sync_model


class Project(BaseModel):
    gid = models.CharField(
        max_length=32,
        unique=True,
        null=True,
        editable=False,
        verbose_name=_("GID"),
    )
    name = models.CharField(
        max_length=512,
        verbose_name=_("Название проекта")
    )
    workspace = models.ForeignKey(
        'core.Workspace',
        on_delete=models.CASCADE,
        related_name='projects',
        null=True,
        verbose_name=_('Рабочее пространство')
    )

    @property
    def resource_type(self):
        return 'project'

    def sync_remote(self):
        return sync_model.delay(self.id, 'Project')

    class Meta:
        verbose_name = _("Проект")
        verbose_name_plural = _("Проекты")

    def __str__(self):
        return self.name
