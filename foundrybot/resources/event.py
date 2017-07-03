from foundrybot.resource import Resource
from pydash import pick


class EventResource(Resource):
    def __init__(self, secret_key):
        super(secret_key)
        self.resource_name = 'Event'

    def get(self, id):
        res = self.make_request({
            'method': 'GET',
            'params': {'id': id},
            'url': '/events/{id}'
        })
        return res.doc

    def search(self, params):
        res = self.make_request({
            'method': 'GET',
            'params': pick(params, 'limit', 'offset', 'url'),
            'url': '/events'
        })
        return res

    def create(self, params):
        res = self.make_request({
            'method': 'POST',
            'data': pick(params, 'url', 'maxUrls', 'maxAge'),
            'url': '/events'
        })
        return res.doc
