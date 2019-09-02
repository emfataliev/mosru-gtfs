from api.client.dataset_type import DatasetType
from api.client.params.impl.filter import Filter
from api.client.params.impl.top import Top
from api.client.params.params import Params
from api.client.url import Url


def test_url():
    params = Params(Top(100), Filter('route_short_name', '500'))
    dataset_type = DatasetType.routes
    url = Url(
        dataset_type,
        params
    ).build()

    expected_url = 'https://apidata.mos.ru/v1/datasets/60664/rows' \
                   '?%24top=100' \
                   '&%24filter=Cells%2Froute_short_name+eq+500'

    assert url == expected_url
