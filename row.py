from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from data import update_data_row, write_row_to_file, DATE_FORMAT


class Row(BaseModel):
    # Name: str
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


class NewRow(Row):
    def write_row_to_file(self):
        row_dict = self.return_dict()
        write_row_to_file(row_dict)


class UpdateRow(Row):
    # Name: Optional[str] = None
    Date: str
    Open: Optional[float] = None
    High: Optional[float] = None
    Low: Optional[float] = None
    Close: Optional[float] = None
    Volume: Optional[int] = None

    def update_data_with_row(self):
        update_data_row(self.return_dict())
