from api.client.params.api import RequestParam


class ApiKey(RequestParam):

    def __init__(self, arguments):
        self.__api_key = vars(arguments.parse_args()).get('api_key')

    def key_value(self):
        return 'api_key', self.__api_key
