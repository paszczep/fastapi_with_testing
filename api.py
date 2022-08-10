from fastapi import FastAPI, Path
from typing import Union
import json
from data import read_row_by_index, read_row_by_date, read_existing_data_dates, delete_row
from task import get_statistic
from row import NewRow, UpdateRow

app = FastAPI()


@app.delete("/delete")
def drop_row(date_index: Union[str, int]):
    delete_row(date_index)


@app.put("/update")
def update_row(row: UpdateRow):
    row.update_data_with_row()


@app.post("/add")
def add_row(item: NewRow):
    dates = read_existing_data_dates()
    if item.Date in dates:
        return {"Error": "Already exists"}
    else:
        item.write_row_to_file()


@app.get("/existing-dates")
def get_existing_dates() -> str:
    dates = read_existing_data_dates()
    return json.dumps(dates)


@app.get("/get-by-index/{item_id}")
def get_by_index(item_id: int = Path(None, description="row index")) -> str:
    values = read_row_by_index(index=item_id)
    values = json.dumps(values)
    return values


@app.get("/get-by-date")
def get_by_date(date: Union[str, int]) -> str:
    row = read_row_by_date(date)
    row = json.dumps(row)
    return row


@app.get("/get-stat/{month}/{column}/{statistic}")
def get_stat(month: str, column: str, statistic: str) -> float:
    """"""
    statistic = get_statistic(month=month, column=column, statistic=statistic)
    return statistic
