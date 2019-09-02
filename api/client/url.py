import urllib
from string import Template


class Url:

    def __init__(self, dataset_type, params):
        self.__dataset_type = dataset_type
        self.__params = params

    def build(self):
        url_template = Template('https://apidata.mos.ru/v1/datasets/${dataset_type}/rows?${params}')
        return url_template.substitute(
            dataset_type=self.__dataset_type,
            params=urllib.urlencode(self.__params.build())
        )
