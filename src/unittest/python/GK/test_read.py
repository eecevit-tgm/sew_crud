import pytest
import server.site


@pytest.yield_fixture(autouse=True)
def run_around_tests():
    file = open('user.json', "w+")
    file.write('[]')


@pytest.fixture
def client():
    server.site.app.testing = True
    client = server.site.app.test_client()
    yield client


def get_all(client):
    res = client.get('/user')
    assert res.json == {}
