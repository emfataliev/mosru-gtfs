from api.client.params.api import RequestParam


class Skip(RequestParam):

    def __init__(self, number):
        self.__number = number

    def key_value(self):
        return '$skip', self.__number
