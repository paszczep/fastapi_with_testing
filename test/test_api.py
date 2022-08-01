from fastapi.testclient import TestClient
from api import app
from test.test_task import check_keys_presence
import json

client = TestClient(app)


def check_code(response):
    return response.status_code == 200


def test_index():
    response = client.get("get-item/0")
    assert check_code(response)
    assert check_keys_presence(json.loads(response.json()).keys())


def test_date():
    pass


def test_stat():
    pass