from core.api.handlers.base import BaseApiHandler


class Project(BaseApiHandler):
    endpoint = 'projects'

    def get_json_params(self, obj):
        return {
            'data': {
                "name": obj.name,
                "owner": obj.owner.gid
            }
        }
