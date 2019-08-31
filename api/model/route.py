from api.row_cell import RowCell


class Route:

    def __init__(self, route_row):
        self.__id_cell = RowCell(route_row, 'route_id')
        self.__short_name_cell = RowCell(route_row, 'route_short_name')
        self.__long_name_cell = RowCell(route_row, 'route_long_name')
        self.__agency_code_cell = RowCell(route_row, 'agency_code')
        self.__route_type_cell = RowCell(route_row, 'route_type')

    def id(self):
        return self.__id_cell.encoded_value()

    def short_name(self):
        return self.__short_name_cell.value()

    def long_name(self):
        return self.__long_name_cell.value()

    def agency_code(self):
        return self.__agency_code_cell.encoded_value()

    def route_type(self):
        return self.__route_type_cell.encoded_value_as_string()
