from foundrybot.resource import Resource
from pydash import pick


class UrlSnapshotContentResource(Resource):
    def __init__(self, secret_key):
        super(secret_key)
        self.resource_name = 'UrlSnapshotContent'

    def search(self, params):
        return self.make_request({
            'method': 'GET',
            'data': pick(params, 'limit', 'offset', 'query', 'urlSnapshotContentId', 'urlSnapshotId', 'domainCrawlId'),
            'url': '/url-snapshot-contents'
        })
