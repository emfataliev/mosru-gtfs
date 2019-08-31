from api.row_cell import RowCell


class Trip:

    def __init__(self, trip):
        self.__id_cell = RowCell(trip, 'trip_id')
        self.__route_id_cell = RowCell(trip, 'route_id')
        self.__service_id_cell = RowCell(trip, 'service_id')

    def id(self):
        return self.__id_cell.encoded_value()

    def route_id(self):
        return self.__route_id_cell.encoded_value()

    def service_id(self):
        return self.__service_id_cell.encoded_value()
