from api.row_cell import RowCell


class StopTime:

    def __init__(self, stop_time):
        self.__stop_id_cell = RowCell(stop_time, 'stop_id')
        self.__trip_id_cell = RowCell(stop_time, 'trip_id')
        self.__arrival_time_cell = RowCell(stop_time, 'arrival_time')
        self.__departure_time_cell = RowCell(stop_time, 'departure_time')
        self.__stop_sequence_cell = RowCell(stop_time, 'stop_sequence')

    def stop_id(self):
        return self.__stop_id_cell.encoded_value_as_string()

    def trip_id(self):
        return self.__trip_id_cell.encoded_value()

    def arrival_time(self):
        return self.__arrival_time_cell.encoded_value()

    def departure_time(self):
        return self.__departure_time_cell.encoded_value()

    def stop_sequence(self):
        return self.__stop_sequence_cell.value()
