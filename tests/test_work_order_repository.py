import pytest
from  src.api.repository.work_order_repository import WorkOrderRepository
from sqlalchemy.orm import DeclarativeBase
from src.api.model.db_base_model import DBBaseModel
from src.api.model.workorder import WorkOrder

    
@pytest.fixture(scope="class")    
def wo_repository(test_db_session)->WorkOrderRepository:
    return WorkOrderRepository(test_db_session)
       

def test_work_order_list(wo_repository):
    work_orders = wo_repository.list()
    assert len(work_orders) > 0
    assert len(work_orders) == 5
    
def test_get_work_order_by_id(wo_repository):
    test_id = -1
    test_work_order = wo_repository.getWorkOrderById(test_id)
    assert test_work_order is not None
    assert test_work_order.title is not None

    
def test_create_work_order(wo_repository):

    test_work_order = WorkOrder(title="create test")
    test_work_order.title = "Create Work Order Unit Test"
    test_work_order.notes = "Test Notes"
    
    beforeNoWorkOrders = len(wo_repository.list())
    wo_repository.createWorkOrder(test_work_order)
    wo_repository.session.commit()
    afterNoWorkOrders = len(wo_repository.list())
    
    assert afterNoWorkOrders > beforeNoWorkOrders
    assert test_work_order is not None
    assert test_work_order.work_order_id is not None
    assert test_work_order.created_ts is not None
    print('work_order_id: ', test_work_order.work_order_id)


def test_update_work_order(wo_repository):
    test_id = -2
    test_updated_String = "Test Work Order Update Unit Test, timestamp"
    test_update_work_order = wo_repository.getWorkOrderById(test_id)
    test_update_work_order.notes = test_updated_String
      
    updated_work_order = wo_repository.updateWorkOrder(test_update_work_order)
    print("saved notes string: ", updated_work_order.notes)
    assert updated_work_order.updated_ts is not None
    
    

def test_delete_work_order(wo_repository):
    test_delete_id  = -4
    delete_work_order = wo_repository.getWorkOrderById(test_delete_id)
    assert delete_work_order is not None
    wo_repository.deleteWorkOrder(delete_work_order)