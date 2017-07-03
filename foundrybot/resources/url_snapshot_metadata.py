from foundrybot.resource import Resource
from pydash import pick


class UrlSnapshotMetadataResource(Resource):
    def __init__(self, secret_key):
        super(secret_key)
        self.resource_name = 'UrlSnapshotMetadata'

    def search(self, params):
        return self.make_request({
            'method': 'GET',
            'data': pick(params, 'limit', 'offset', 'name', 'content', 'urlSnapshotId', 'domainCrawlId'),
            'url': '/url-snapshot-metadata'
        })
