import pandas as pd
from pandas import DataFrame as DataFrame
from typing import Union
from src.data import read_data


def get_statistic(month: Union[str, pd.Timestamp], column: str, statistic: str) -> float:
    data = read_data()
    selected_series = data.loc[data.index.to_period('M') == month, column]

    mapping = {
        'min': DataFrame.min,
        'max': DataFrame.max,
        'mean': DataFrame.mean,
        'median': DataFrame.median}

    result = mapping[statistic](selected_series)
    result = round(result, 2)
    return result
