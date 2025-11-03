from pydantic import BaseModel
from typing import List

class LineChart(BaseModel):
    xData: List[str]
    yData: List[int]