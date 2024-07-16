from fastapi import FastAPI

from fastapi import APIRouter, Depends, HTTPException

from ..schema.work_order_schema import WorkOrder 
import datetime

router = APIRouter()

work_order_1 ={
    'work_order_id': 1,
    'title': 'test',
    'start_date' : str(datetime.date(2023, 12, 25))
}

work_order_schema1 = WorkOrder(**work_order_1)
work_orders = [work_order_schema1]
work_order ={'single work order'}


@router.get("/workorders")
def getWorkOrders():
    return "test 1"

@router.get("/workorder/{work_order_id}")
def get_work_order():
    return work_order_schema1

@router.post("/workorder/{work_order_id}")
def create_work_order():
    pass

router.put("/workorder/{work_order_id}")
def update_work_order():
    pass

router.delete("/workorder/{work_order_id}")
def delete_work_order():
    pass