from pydantic import BaseModel
from datetime import datetime
from src.api.schema.task_schema import Task

class WorkOrderSchema(BaseModel):
    work_order_id: int
    project_id: int | None = None
    title: str | None = None
    site: str | None = None
    tasks: list[Task] | None = None
    start_date: str | None = None
    end_date: str | None = None
