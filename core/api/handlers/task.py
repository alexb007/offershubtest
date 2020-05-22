from django.apps import apps

from core.api.handlers.base import BaseApiHandler


class Task(BaseApiHandler):
    endpoint = 'tasks'

    def get_json_params(self, obj):
        return {
            'data': {
                "name": obj.name,
                "projects": obj.projects.all().values_list('gid', flat=True),
            }
        }
