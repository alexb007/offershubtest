from core.api.handlers.base import BaseApiHandler


class User(BaseApiHandler):
    endpoint = 'users'

    def get_json_params(self, obj):
        return {
            'data': {
                "name": obj.name,
            }
        }

    def getMe(self):
        return self.action('me')

    def getWorkspaces(self):
        return self.client.workspaces.find_all()
