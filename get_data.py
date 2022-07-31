import pandas as pd
import json

INPUT_FILE_PATH = "data.csv"
DATA_COLS_LIST = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']


def get_data() -> pd.DataFrame:
    df = pd.read_csv(INPUT_FILE_PATH, index_col="Date", parse_dates=True)
    return df


def get_data_row(index: int) -> str:
    df = get_data().reset_index()
    row_dict = df.iloc[index].to_dict()
    return json.dumps(row_dict, default=str)
