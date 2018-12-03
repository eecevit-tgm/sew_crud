import pytest
import server.site


@pytest.fixture
def client():
    server.site.app.testing = True
    client = server.site.app.test_client()
    yield client


def test_readall(client):
    res = client.get('/user')
    assert res.json == [{"username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "ds"},{"username":  "dsunaric", "email":  "dsunaric@student.tgm.ac.at", "picture": "link"}]


def test_singleUser(client):
    res = client.get('/user/eecevit')
    assert res.json == [{"username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "ds"}]