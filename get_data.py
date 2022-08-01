import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE_PATH = BASE_DIR / "data.csv"
DATA_COLS_LIST = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']


def get_data() -> pd.DataFrame:
    df = pd.read_csv(INPUT_FILE_PATH, index_col="Date", parse_dates=True)
    return df


def get_row_by_index(index: int) -> str:
    df = get_data().reset_index()
    row_dict = df.iloc[index].to_dict()
    return json.dumps(row_dict, default=str)


def get_row_by_date(date: str) -> str:
    df = get_data().reset_index()
    row_dict = df.loc[df.Date == date].to_dict()
    return json.dumps(row_dict, default=str)