from sqlalchemy import Column
from sqlalchemy import Identity
from sqlalchemy import TIMESTAMP,FetchedValue
from src.api.model.db_base_model import DBBaseModel
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.schema import Sequence
from sqlalchemy import DateTime
from datetime import datetime

class WorkOrder(DBBaseModel):
    __tablename__ = "work_order"
    work_order_id = Column("work_order_id", Sequence("work_order_work_order_id_seq"), primary_key=True)
    title = Column("title")
    notes: Mapped[str] = mapped_column("notes")
    start_date: Mapped[datetime] = mapped_column("start_date")
    end_date: Mapped[datetime] = mapped_column("end_date")
    site_location_id: Mapped[int] = mapped_column("site_location_id")
    order_source: Mapped[str] = mapped_column("order_source")
    recieved_by: Mapped[int] = mapped_column("recieved_by")
    approved_id: Mapped[int] = mapped_column("approved_id")
    created_by: Mapped[int] = mapped_column("created_by")
    created_ts: Mapped[datetime] = mapped_column("created_ts", DateTime, default=datetime.now())
    updated_by: Mapped[int] = mapped_column("updated_by")
    updated_ts: Mapped[datetime] = mapped_column("updated_ts") 
    