from api.client.params.params import Params
from api.client.params.impl.top import Top
from api.client.params.impl.filter import Filter
from api.client.params.impl.api_key import ApiKey
from api.client.url import Url
from api.client.dataset_type import DatasetType


def test_url():
    params = Params(
        Top(100),
        Filter('route_short_name', '500'),
        ApiKey('*'))

    url = Url(
        DatasetType.routes,
        params
    ).build()

    expected_url = 'https://apidata.mos.ru/v1/datasets/60664/rows' \
                   '?%24top=100' \
                   '&%24filter=Cells%2Froute_short_name+eq+500' \
                   '&api_key=%2A'

    assert url == expected_url
