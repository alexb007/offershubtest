from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel
from core.tasks import sync_model


class Task(BaseModel):
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
    assignee = models.ForeignKey(
        'core.AsanaUser',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name=_('Исполнитель')
    )
    projects = models.ManyToManyField(
        'core.Project',
        related_name='tasks',
        verbose_name=_("Проекта")
    )
    notes = models.TextField(
        max_length=3000,
        verbose_name=_('Текст задачи')
    )

    def sync_remote(self):
        return sync_model.delay(self.id, 'Task')

    @property
    def resource_type(self):
        return 'task'

    class Meta:
        verbose_name = _("Задача")
        verbose_name_plural = _("Задачи")

    def __str__(self):
        return self.name
