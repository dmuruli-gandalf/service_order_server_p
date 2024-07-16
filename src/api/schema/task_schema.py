from datetime import datetime
from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    task_id: int
    work_order_id: int
    start_date: str | None = None
    end_date: datetime| None = None
    title: str | None = None
    notes: str | None = None
    work_order_id: int
    supplies: List[int] | None

