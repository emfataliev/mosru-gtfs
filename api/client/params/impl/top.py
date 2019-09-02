from api.client.params.api import RequestParam


class Top(RequestParam):

    def __init__(self, batch_size):
        self.__batch_size = batch_size

    def key_value(self):
        return '$top', self.__batch_size
