from fastapi.testclient import TestClient
from src.api import app
from random import choice
from .test_task import check_keys_presence, check_values, read_row_by_date, check_row_value_data_types
import json

client = TestClient(app)


def check_status_code(response):
    return response.status_code == 200


def get_stat_value(month: str, column: str, statistic: str):
    response = client.get(f"get-stat/{month}/{column}/{statistic}")
    return round(float(response.text), 2)


def test_index():
    response = client.get("get-by-index/0")
    assert check_status_code(response)
    response_keys = json.loads(response.json()).keys()
    assert check_keys_presence(response_keys)
    assert check_row_value_data_types(json.loads(response.json()))


def test_date():
    existing_dates = client.get("existing-dates")
    assert check_status_code(existing_dates)

    existing_dates = json.loads(existing_dates.json())
    date_choice = choice(existing_dates)
    response = client.get(f"get-by-date?date={date_choice}")
    assert check_status_code(response)

    response_keys = json.loads(response.json()).keys()
    assert check_keys_presence(response_keys)

    response_row = json.loads(response.json())
    direct_row = read_row_by_date(date_choice)
    assert response_row == direct_row

# ToDo Check stat, add, delete, update
# def test_stat():
#     assertion = check_values(get_stat_value)
#     assert assertion
#
#
# def test_add():
#     pass