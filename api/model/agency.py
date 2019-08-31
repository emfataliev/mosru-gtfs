from api.row_cell import RowCell


class Agency:

    def __init__(self, agency_row):
        self.__name_cell = RowCell(agency_row, 'agency_name')
        self.__code_cell = RowCell(agency_row, 'agency_code')
        self.__url_cell = RowCell(agency_row, 'agency_url')
        self.__time_zone_cell = RowCell(agency_row, 'agency_timezone')

    def name(self):
        return self.__name_cell.value()

    def code(self):
        return self.__code_cell.encoded_value()

    def url(self):
        return self.__url_cell.encoded_value()

    def time_zone(self):
        return self.__time_zone_cell.encoded_value()
