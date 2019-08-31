from api.row_cell import RowCell


class Coordinates:

    def __init__(self, row):
        self.__geo_data_cell = RowCell(row, 'geoData')

    def lat(self):
        return self.__geo_data_cell.value()['coordinates'][0]

    def lng(self):
        return self.__geo_data_cell.value()['coordinates'][1]
