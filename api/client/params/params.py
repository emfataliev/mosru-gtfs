class Params:
    def __init__(self, *request_param):
        self.__request_params = request_param

    def build(self):
        return list(map(lambda request_param: request_param.key_value(), self.__request_params))
