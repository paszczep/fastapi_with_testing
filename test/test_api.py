from fastapi.testclient import TestClient
from api import app
from test.test_task import check_keys_presence
import json

client = TestClient(app)


def check_code(response):
    return response.status_code == 200


def test_index():
    response = client.get("get-by-index/0")
    assert check_code(response)
    response_keys = json.loads(response.json()).keys()
    assert check_keys_presence(response_keys)


def test_date():
    response = client.get("get-by-date?date=2016-07-22")
    assert check_code(response)
    response_keys = json.loads(response.json()).keys()
    assert check_keys_presence(response_keys)


def test_stat():
    response = client.get("get-stat/2017-07/High/max")
    assert check_code(response)
    # print(response.text)
    # assert