import pytest
from server import app
from webtest import TestApp as TA

@pytest.fixture(scope='module')
def application():
    test_app = TA(app)
    return test_app

def test_python_ireland_shold_be_in_response_body(application):
    response = application.get('/')
    assert b'Hi!' == response.body

def test_response_shold_be_ok(application):
    response = application.get('/')
    assert response.status == "200 OK"

def test_response_status_code_shold_be_200(application):
    response = application.get('/')
    assert response.status_int == 200
