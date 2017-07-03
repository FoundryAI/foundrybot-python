from foundrybot.resource import Resource
from pydash import pick


class UrlSnapshotTagResource(Resource):
    def __init__(self, secret_key):
        super(secret_key)
        self.resource_name = 'UrlSnapshotTag'

    def search(self, params):
        return self.make_request({
            'method': 'GET',
            'data': pick(params, 'limit', 'offset', 'tag', 'urlSnapshotId', 'domainCrawlId'),
            'url': '/url-snapshot-tags'
        })
