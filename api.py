from fastapi import FastAPI, Path
from get_data import get_row_by_index, get_row_by_date, DATA_LENGTH
from task import get_statistic

app = FastAPI()


@app.get("/data-length")
def home() -> int:
    return DATA_LENGTH


@app.get("/get-by-index/{item_id}")
def get_by_index(item_id: int = Path(None, description="row index")) -> str:
    values = get_row_by_index(index=item_id)
    return values


@app.get("/get-by-date")
def get_by_date(date: str) -> str:
    row = get_row_by_date(date)
    return row


@app.get("/get-stat/{month}/{column}/{stat}")
def get_stat(month: str, column: str, statistic: str) -> float:
    statistic = get_statistic(month=month, column=column, statistic=statistic)
    return statistic
