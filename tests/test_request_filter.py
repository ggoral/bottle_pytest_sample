import pytest
import request_filter


@pytest.fixture(scope='module')
def application():
    pass
    #test_app = TA(app)
    #return test_app

def test_request_filter_size(application):
    data = {}
    request_filter.filter_data(data)
    assert len(data) == 3
