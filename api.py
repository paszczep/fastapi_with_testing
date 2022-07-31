from fastapi import FastAPI
from get_data import get_data_row
from task import get_statistic

app = FastAPI()


# @app.get("/")
# def home():
#     return 'home'


@app.get("/get-item/{item_id}")
def get_item(item_id: int) -> str:
    values = get_data_row(index=item_id)
    return values


@app.get("/get-stat/{month}/{column}/{stat}")
def get_stat(month: str, column: str, stat: str) -> float:
    statistic = get_statistic(month=month, col=column, stat=stat)
    return statistic
