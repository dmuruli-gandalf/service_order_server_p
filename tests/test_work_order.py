from configtest import test_db
from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.api.main import app
import json



client = TestClient(app)

def  test_config_list_work_orders():
    response = client.get("/workorders")
    assert response.status_code == 200
    print("work order response: ", response.json)
    
def test_work_order_api():
    response = client.get("/workorder/1")
    assert response.status_code == 200
    data = response.content
    payload = response.json
    work_order_dict = json.loads(response.content)
    id = work_order_dict['work_order_id']
    assert id == 1
    print('Test retrieve work order with id=', id)
    print("workorder response: ", data)
    print("payload, ", payload)
    
    
def test_load_data(test_db):
    val = test_db
    print(val)
   
