import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE_PATH = BASE_DIR / "data.csv"
DATA_COLS_LIST = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

data = pd.read_csv(INPUT_FILE_PATH, index_col="Date", parse_dates=True)
DATA_LENGTH = len(data)


def get_data() -> pd.DataFrame:
    return data


def get_row_by_index(index: int) -> str:
    df = get_data().reset_index()
    row = df.iloc[index]
    row_dict = row.to_dict()
    row_dict['Date'] = row_dict['Date'].strftime('%Y-%m-%d')
    row_dict['Volume'] = int(row_dict['Volume'])
    return json.dumps(row_dict)


def get_row_by_date(date: str) -> str:
    df = get_data().reset_index()
    row = df.loc[df.Date == date]
    row_dict = row.to_dict(orient='records').pop()
    row_dict['Date'] = row_dict['Date'].strftime('%Y-%m-%d')
    return json.dumps(row_dict)
