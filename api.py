from fastapi import FastAPI, Path
import json
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from get_data import DATE_FORMAT, get_row_by_index, get_row_by_date, get_all_dates, write_row
from task import get_statistic

app = FastAPI()


class Row(BaseModel):
    Name: str
    Date: Optional[str] = datetime.now().strftime(DATE_FORMAT)
    Open: float
    High: float
    Low: float
    Close: float
    Volume: int

    def return_dict(self) -> dict:
        row_dict = {'Date': self.Date,
                    'Open': round(self.Open, 4),
                    'High': round(self.High, 4),
                    'Low': round(self.Low, 4),
                    'Close': round(self.Close, 4),
                    'Volume': self.Volume}
        return row_dict


# @app.put("/update")
# def update_row():
#     pass


@app.post("/add")
def add_row(item: Row):
    dates = get_all_dates()
    if item.Date in dates:
        return {"Error": "Already exists"}
    else:
        write_row(item.return_dict())


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
