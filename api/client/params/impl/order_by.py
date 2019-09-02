from api.client.params.api import RequestParam


class OrderBy(RequestParam):

    def __init__(self, cell_name):
        self.__cell_name = cell_name

    def key_value(self):
        return '$orderby', self.__cell_name
