from task import get_statistic
import pandas as pd
import os
import json
from get_data import INPUT_FILE_PATH, DATA_COLS_LIST, get_data, get_data_row

test_data = pd.read_csv('tests.csv')


def test_task():
    test_data['result'] = test_data.apply(
        lambda row: get_statistic(month=row['month'], col=row['col'], stat=row['stat']), axis=1)
    assertion = test_data['result'].equals(test_data['output'])
    assert assertion


def elements_presence(data):
    tests = [False for el in DATA_COLS_LIST if el not in data]
    return all(tests)


def test_get_data():
    assert os.path.isfile(INPUT_FILE_PATH)
    data_columns = get_data().reset_index().columns
    assert elements_presence(data_columns)


def test_get_data_row():
    row = get_data_row(0)
    row = json.loads(row)
    assert elements_presence(row.keys())

