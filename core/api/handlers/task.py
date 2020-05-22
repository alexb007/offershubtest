from core.api.handlers.base import BaseApiHandler


class Task(BaseApiHandler):
    endpoint = 'tasks'

    def get_json_params(self, obj):
        return {
            "name": obj.name,
            "assignee": obj.assignee.gid,
            "projects": list(obj.projects.all().values_list('gid', flat=True)),
            "notes": obj.notes,
        }
