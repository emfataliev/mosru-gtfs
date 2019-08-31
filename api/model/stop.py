from api.model.coordinates import Coordinates
from api.row_cell import RowCell


class Stop:

    def __init__(self, stop_row):
        self.__id_cell = RowCell(stop_row, 'stop_id')
        self.__stop_name_cell = RowCell(stop_row, 'stop_name')
        self.__coordinates = Coordinates(stop_row)

    def id(self):
        return self.__id_cell.encoded_value_as_string()

    def stop_name(self):
        return self.__stop_name_cell.value()

    def coordinates(self):
        return self.__coordinates
