from src.api.schema.work_order_schema import WorkOrder

class work_order_service():
    def get_work_orders(project_id: int)->list[WorkOrder]:
        pass
    
    def get_work_order(work_id: int)->WorkOrder:
        pass
    
    def update_work_order(work_order: WorkOrder)->WorkOrder:
        pass
    
    def create_work_order(work_order: WorkOrder)->WorkOrder:
        pass
    
    def delete_work_order(work_order: WorkOrder)->bool:
        pass
    
    