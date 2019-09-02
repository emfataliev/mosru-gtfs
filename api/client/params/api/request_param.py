from abc import abstractmethod, ABCMeta


class RequestParam(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def key_value(self):
        return
