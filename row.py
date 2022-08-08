import csv
# from pandas import DataFrame
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from get_data import DATE_FORMAT, INPUT_FILE_PATH, DATA_COLS


# class Row():
#    def return_dict


class NewRow(BaseModel):
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

    def write_row_to_file(self):
        row_dict = self.return_dict()
        with open(INPUT_FILE_PATH, 'a', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=DATA_COLS)
            writer.writerow(rowdict=row_dict)


class UpdateRow(BaseModel):
    Name: Optional[str] = None
    Date: Optional[str] = None
    Open: Optional[float] = None
    High: Optional[float] = None
    Low: Optional[float] = None
    Close: Optional[float] = None
    Volume: Optional[int] = None

    # def return_dict(self):
    #     row_dict = self.NewRow.return_dict()
    #     return row_dict
