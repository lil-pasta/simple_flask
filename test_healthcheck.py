from app import create_app
from flask import url_for
from app.main.forms import LandingPageForm
import pytest
import json

#####################
# Integration Tests #
#####################

# fixtures are reused by the pytest module during tests
# which saves on boilerplate code to spin up a new app for each
# test you might write. Tests can also be separated into modules.
#
# to run type pytest into your cmd
@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    with app.test_request_context():
        with app.test_client() as client:
            yield client

# your function has to begin with the word test for pytest to identify it
def test_health_check(client):
    tc = client.get(url_for('main.health_check'))
    assert 200 == tc.status_code

# slightly more complicated test
def test_concat_function_success(client):
    tc = client.post(url_for('main.index'), data={"word_one": "hello", "word_two": " bitchboy"}, follow_redirects=True)
    assert 200 == tc.status_code
    assert b'hello bitchboy' in tc.data


