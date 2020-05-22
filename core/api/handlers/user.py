from core.api.handlers.base import BaseApiHandler


class User(BaseApiHandler):
    endpoint = 'users'

    def get_json_params(self, obj):
        return {
            'data': {
                "name": obj.name,
            }
        }
