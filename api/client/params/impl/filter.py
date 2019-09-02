from api.client.params.api import RequestParam


class Filter(RequestParam):

    def __init__(self, cell_name, cell_value):
        self.__cell_name = cell_name
        self.__cell_value = cell_value

    def key_value(self):
        return '$filter', 'Cells/' + self.__cell_name + ' eq ' + str(self.__cell_value)
