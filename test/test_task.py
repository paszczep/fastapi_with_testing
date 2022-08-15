from src.task import get_statistic
import pandas as pd
import os
from typing import Callable
from pathlib import Path
from src.data import INPUT_FILE_PATH, DATA_COLS, BASE_DIR, read_data, read_row_by_index, read_row_by_date

# ToDo Separate test dataset
# test_data = pd.read_csv('test\\tests.csv')


def get_test_data(base_dir: Path = BASE_DIR) -> pd.DataFrame:
    test_data_file = base_dir / 'test' / 'tests.csv'
    test_data = pd.read_csv(test_data_file)
    return test_data


def check_values(func: Callable) -> bool:
    test_data = get_test_data()
    test_data['result'] = test_data.apply(
        lambda row: func(month=row['month'], column=row['col'], statistic=row['stat']), axis=1)
    assertion = test_data['result'].equals(test_data['output'])
    return assertion


def test_task_direct():
    assertion = check_values(get_statistic)
    assert assertion


def check_keys_presence(keys_list: list) -> bool:
    tests = [False for el in DATA_COLS if el not in keys_list]
    return all(tests)


def test_get_data_file():
    assert os.path.isfile(INPUT_FILE_PATH)
    data_columns = read_data().reset_index().columns
    assert check_keys_presence(data_columns)


def check_row_keys(row: dict) -> bool:
    return check_keys_presence(list(row.keys()))


def test_get_data_row_by_index():
    row = read_row_by_index(0)
    assert check_row_keys(row)


def test_get_data_row_by_date():
    # ToDo actually read row by date_index, check value types
    row = read_row_by_date('0')
    assert check_row_keys(row)
