from api.client.params.api import RequestParam


class ApiKey(RequestParam):

    def __init__(self, api_key):
        self.__api_key = api_key

    def key_value(self):
        return 'api_key', self.__api_key
