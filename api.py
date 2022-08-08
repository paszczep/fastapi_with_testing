from fastapi import FastAPI, Path
import json
from get_data import get_row_by_index, get_row_by_date, get_all_dates
from task import get_statistic
from row import NewRow, UpdateRow

app = FastAPI()


@app.put("/update/{date_index}")
def update_row(date_index: str, row: UpdateRow):
    print(date_index, UpdateRow.return_dict())


@app.post("/add")
def add_row(item: NewRow):
    dates = get_all_dates()
    if item.Date in dates:
        return {"Error": "Already exists"}
    else:
        item.write_row_to_file()


@app.get("/existing-dates")
def get_existing_dates() -> str:
    dates = get_all_dates()
    return json.dumps(dates)


@app.get("/get-by-index/{item_id}")
def get_by_index(item_id: int = Path(None, description="row index")) -> str:
    values = get_row_by_index(index=item_id)
    values = json.dumps(values)
    return values


@app.get("/get-by-date")
def get_by_date(date: str) -> str:
    row = get_row_by_date(date)
    row = json.dumps(row)
    return row


@app.get("/get-stat/{month}/{column}/{statistic}")
def get_stat(month: str, column: str, statistic: str) -> float:
    statistic = get_statistic(month=month, column=column, statistic=statistic)
    return statistic
