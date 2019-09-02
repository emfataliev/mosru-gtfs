ENCODING = 'utf-8'


class RowCell:

    def __init__(self, row, cell_name):
        self.__row = row
        self.__cell_name = cell_name

    def value(self):
        return self.__row['Cells'][self.__cell_name]

    def encoded_value(self):
        return self.value().encode(ENCODING)

    def encoded_string_value(self):
        return str(self.value()).encode(ENCODING)
