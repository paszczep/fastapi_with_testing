import pandas as pd
from pandas import DataFrame
from pathlib import Path
from csv import DictWriter

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE_PATH = BASE_DIR / "data.csv"
DATA_COLS = ('Date', 'Open', 'High', 'Low', 'Close', 'Volume')
INDEX_COL = 'Date'
DATE_FORMAT = '%Y-%m-%d'


def write_row_to_file(row_dict: dict, data_file_path: Path = INPUT_FILE_PATH):
    data_file_path = str(data_file_path.resolve())
    with open(data_file_path, 'a', encoding='UTF8', newline='') as f:
        writer = DictWriter(f, fieldnames=DATA_COLS)
        writer.writerow(rowdict=row_dict)


def save_to_file(*, file_path: Path = INPUT_FILE_PATH, data: DataFrame):
    data.to_csv(file_path)


def update_data_row(row_dict: dict) -> DataFrame:
    row_dict = {key: value for key, value in row_dict.items() if value is not None}
    row_index = row_dict.pop(INDEX_COL)
    data = pd.read_csv(INPUT_FILE_PATH, index_col=INDEX_COL)
    data_index = data.loc[data.index == row_index, list(row_dict.keys())].index
    archive_values = data.loc[data.index == str(data_index)]
    data.loc[data_index, list(row_dict.keys())] = row_dict.values()
    save_to_file(data=data)
    # ToDo Archive un-updated record
    return archive_values


def read_csv_data_file(file_path: Path = INPUT_FILE_PATH, **kwargs) -> DataFrame:
    data = pd.read_csv(file_path, index_col=INDEX_COL, **kwargs)
    return data


def delete_row(date_index):
    data = read_csv_data_file()
    drop_row = data.drop(index=date_index, inplace=True)
    save_to_file(data=data)
    print(drop_row)
    return drop_row


def read_data(usecols: set = DATA_COLS) -> DataFrame:
    data = read_csv_data_file(usecols=list(usecols), parse_dates=True)
    return data


def read_existing_data_dates() -> list:
    available_dates = read_csv_data_file(usecols=[INDEX_COL], parse_dates=False).index
    return list(available_dates)


def read_row_by_index(index: int) -> dict:
    df = read_data().reset_index()
    row = df.iloc[index]
    row_dict = row.to_dict()
    row_dict['Date'] = row_dict['Date'].strftime(DATE_FORMAT)
    row_dict['Volume'] = int(row_dict['Volume'])
    return row_dict


def read_row_by_date(date: str) -> dict:
    df = read_data()
    row = df.loc[df.index == date].reset_index()
    row_dict = row.to_dict(orient='records').pop()
    row_dict['Date'] = row_dict['Date'].strftime(DATE_FORMAT)
    return row_dict
