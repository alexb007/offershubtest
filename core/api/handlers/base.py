import asana
from django.conf import settings


class BaseApiHandler:
    endpoint = None
    requester = None

    def __init__(self):
        self.client = asana.Client.access_token(settings.ASANA_API_TOKEN)

    def get_json_params(self, obj):
        raise NotImplementedError('get_json_params method is not implemented!')

    def handle_response(self, response):
        print(response)
        return response

    def action(self, method_name, *args, **kwargs):
        _endpoint = self.endpoint
        if _endpoint is None:
            raise Exception('Endpoint not defined!')
        endpoint = getattr(self.client, _endpoint)
        method = getattr(endpoint, method_name)
        print(method)
        if method is None or not callable(method):
            raise Exception(f'{method_name} not found or not acceptable for this endpoint!')
        response = method(*args, **kwargs)
        return self.handle_response(response)

    def create(self, obj, **options):
        json_params = self.get_json_params(obj)
        return self.action('create', params=json_params, options=options)

    def update(self, obj, **options):
        json_params = self.get_json_params(obj)
        return self.action('update', obj.gid, params=json_params, options=options)
