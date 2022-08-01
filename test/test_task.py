from task import get_statistic
import pandas as pd
import os
import json
from typing import Callable
from get_data import INPUT_FILE_PATH, DATA_COLS_LIST, get_data, get_row_by_index

# test_data = pd.read_csv('test\\tests.csv')


def check_values(test_data: pd.DataFrame, func: Callable) -> bool:
    test_data['result'] = test_data.apply(
        lambda row: func(month=row['month'], column=row['col'], statistic=row['stat']), axis=1)
    assertion = test_data['result'].equals(test_data['output'])
    return assertion


def test_task_direct():
    test_data = pd.read_csv('test\\tests.csv')
    assertion = check_values(test_data, get_statistic)
    assert assertion


def check_keys_presence(keys_list: list) -> bool:
    tests = [False for el in DATA_COLS_LIST if el not in keys_list]
    return all(tests)


def test_get_data_file():
    assert os.path.isfile(INPUT_FILE_PATH)
    data_columns = get_data().reset_index().columns
    assert check_keys_presence(data_columns)


def check_data_row(row: str) -> bool:
    row = json.loads(row)
    return check_keys_presence(row.keys())


def test_get_data_row_by_index():
    row = get_row_by_index(0)
    assert check_data_row(row)


def get_existing_date():
    pass


def test_get_data_row_by_date():
    row = get_row_by_index(0)
    assert check_data_row(row)
