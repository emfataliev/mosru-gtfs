from api.client.params.impl.filter import Filter
from api.client.params.impl.order_by import OrderBy
from api.client.params.impl.skip import Skip
from api.client.params.impl.top import Top
from api.client.params.params import Params


def test_params():
    params = Params(
        Top(100),
        Skip(10),
        Filter('type', 'BUS'),
        OrderBy('price')
    ).build()

    expected_params = [
        ('$top', 100),
        ('$skip', 10),
        ('$filter', 'Cells/type eq BUS'),
        ('$orderby', 'price')
    ]

    assert params == expected_params
