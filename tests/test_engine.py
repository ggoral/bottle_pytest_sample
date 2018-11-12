import pytest
import engine


@pytest.fixture(scope='module')
def application():
    pass
    #test_app = TA(app)
    #return test_app

def test_reactor_work(application):
    assert engine.reactor()
