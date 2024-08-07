import datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy import select
from sqlalchemy.exc import DatabaseError


from src.api.schema.work_order_schema import WorkOrderSchema
from src.api.model.workorder import WorkOrder

class WorkOrderRepository:#
    def __init__(self, session):
        self.session = session
      
    def list(self)-> List[Optional[WorkOrderSchema]]: 
        work_orders = self.session.query(WorkOrder).all()
        return [WorkOrderSchema(**work_order.__dict__) for work_order in work_orders]
    
    def createWorkOrder(self, workOrder)->WorkOrder:
        self.session.add(workOrder)
        

    def getWorkOrderById(self, workOrderId)->WorkOrder:
        return self.session.get(WorkOrder,workOrderId)
    
    def updateWorkOrder(self, workOrder)->WorkOrder:
        dbWorkOrder = self.session.get(WorkOrder,workOrder.work_order_id)
        if dbWorkOrder is None:
            raise DatabaseError("Work Order with id: ", workOrder.work_order_id, " does not exist")
        
        dbWorkOrder.title = workOrder.title
        dbWorkOrder.notes = workOrder.notes
        dbWorkOrder.start_date = workOrder.start_date
        dbWorkOrder.end_date  = workOrder.end_date
        dbWorkOrder.site_location_id = workOrder.site_location_id
        dbWorkOrder.order_source = workOrder.order_source
        dbWorkOrder.recieved_by = workOrder.recieved_by
        dbWorkOrder.approved_id = workOrder.approved_id
        dbWorkOrder.created_by = workOrder.created_by
        dbWorkOrder.created_ts = workOrder.created_ts
        dbWorkOrder.updated_by = workOrder.updated_by
        dbWorkOrder.updated_ts = datetime.datetime.now()
           
        self.session.add(dbWorkOrder)
        self.session.flush()
        return dbWorkOrder

    
    def deleteWorkOrder(self, workOrderId)->None:       
        stmt = select(WorkOrder).where(WorkOrder.work_order_id == workOrderId)
        deletionWorkOrder = self.session.scalars(stmt).first()
        if deletionWorkOrder is None:
            raise DatabaseError("Work Order with work order id: ", workOrderId, "does not exist, so cannot delete")
        
        self.session.delete(deletionWorkOrder)
        self.session.flush()
        
        
    