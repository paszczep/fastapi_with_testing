import pandas as pd
import json
from pathlib import Path
from typing import Union

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE_PATH = BASE_DIR / "data.csv"
DATA_COLS = ('Date', 'Open', 'High', 'Low', 'Close', 'Volume')
INDEX_COL = 'Date'
DATE_FORMAT = '%Y-%m-%d'


def get_data(file_path: Path = INPUT_FILE_PATH, usecols: set = DATA_COLS) -> pd.DataFrame:
    data = pd.read_csv(file_path, usecols=list(usecols), index_col=INDEX_COL, parse_dates=True)
    return data


def get_available_dates(file_path: Path = INPUT_FILE_PATH) -> list:
    available_dates = pd.read_csv(file_path, usecols=[INDEX_COL], index_col=INDEX_COL, parse_dates=False)
    return list(available_dates.index)


def get_row_by_index(index: int) -> dict:
    df = get_data().reset_index()
    row = df.iloc[index]
    row_dict = row.to_dict()
    row_dict['Date'] = row_dict['Date'].strftime(DATE_FORMAT)
    row_dict['Volume'] = int(row_dict['Volume'])
    return row_dict


def get_row_by_date(date: str) -> dict:
    df = get_data().reset_index()
    row = df.loc[df.Date == date]
    row_dict = row.to_dict(orient='records').pop()
    row_dict['Date'] = row_dict['Date'].strftime(DATE_FORMAT)
    return row_dict
