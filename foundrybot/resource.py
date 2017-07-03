from pydash import map_keys
from requests import Request, Session
from foundrybot.error import FoundrybotError

class Resource:
    def __init__(self, secret_key):
        """
        :param secret_key: API secret key
        """
        self.secret_key = secret_key

        if self.secret_key is None:
            raise FoundrybotError('Missing required "secretKey".', 'authentication_error')

    def make_request(self, requestConfig):
        """
        Abstracted request method, request config is defined in the resource itself
        :param requestConfig:
        :return:
        """
        session = Session()
        req = Request(
            requestConfig.method,
            'https://api.foundrybot.com/v1' + self.build_url(requestConfig),
            auth=(self.secret_key, ''),
            data=requestConfig.data,
            params=requestConfig.query
        )
        prepared = req.prepare()
        prepared.headers['User-Agent'] = 'Foundrybot python v1.0.0 +(https://github.com/FoundryAI/foundrybot-python#readme)'
        return session.send(prepared).json()

    def build_url(requestConfig):
        """
        Build the url path string
        :return url:
        """
        url = requestConfig.url
        map_keys(requestConfig.params, lambda value, key: url.replace('{' + key + '}', value))
        return url
