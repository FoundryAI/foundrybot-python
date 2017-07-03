from foundrybot.resource import Resource
from pydash import pick


class UrlSnapshotResource(Resource):
    def __init__(self, secret_key):
        super(secret_key)
        self.resource_name = 'UrlSnapshot'

    def get(self, id):
        res = self.make_request({
            'method': 'GET',
            'params': {'id': id},
            'url': '/url-snapshots/{id}'
        })
        return res.doc

    def search(self, params):
        return self.make_request({
            'method': 'GET',
            'data': pick(params, 'limit', 'offset', 'urlHref', 'domainHostname'),
            'url': '/url-snapshots'
        })
