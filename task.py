import pandas as pd
from typing import Union
from get_data import get_data


def get_statistic(month: Union[str, pd.Timestamp], col: str, stat: str) -> float:
    df = get_data()
    selected_series = df.loc[df.index.to_period('M') == month, col]

    mapping = {
        'min': pd.DataFrame.min,
        'max': pd.DataFrame.max,
        'mean': pd.DataFrame.mean,
        'median': pd.DataFrame.median}

    result = mapping[stat](selected_series)
    result = round(result, 2)
    return result
