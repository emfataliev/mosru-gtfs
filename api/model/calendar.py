from datetime import datetime

from api.row_cell import RowCell


class Calendar:

    def __init__(self, calendar_row):
        self.__id_cell = RowCell(calendar_row, 'service_id')
        self.__start_date_cell = RowCell(calendar_row, 'start_date')
        self.__end_date_cell = RowCell(calendar_row, 'end_date')
        self.__monday_cell = RowCell(calendar_row, 'monday')
        self.__tuesday_cell = RowCell(calendar_row, 'tuesday')
        self.__wednesday_cell = RowCell(calendar_row, 'wednesday')
        self.__thursday_cell = RowCell(calendar_row, 'thursday')
        self.__friday_cell = RowCell(calendar_row, 'friday')
        self.__saturday_cell = RowCell(calendar_row, 'saturday')
        self.__sunday_cell = RowCell(calendar_row, 'sunday')

    def is_actual(self):
        calendar_date = datetime.strptime(self.__end_date_cell.encoded_value(), '%Y%m%d')
        return calendar_date > datetime.now()

    def is_not_actual(self):
        return not self.is_actual()

    def fields(self):
        return [
            self.__id_cell.encoded_value(),
            self.__start_date_cell.encoded_value(),
            self.__end_date_cell.encoded_value(),
            self.__monday_cell.encoded_string_value(),
            self.__tuesday_cell.encoded_string_value(),
            self.__wednesday_cell.encoded_string_value(),
            self.__thursday_cell.encoded_string_value(),
            self.__friday_cell.encoded_string_value(),
            self.__saturday_cell.encoded_string_value(),
            self.__sunday_cell.encoded_string_value(),
        ]
