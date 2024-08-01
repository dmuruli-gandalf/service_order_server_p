import os
import pytest
import subprocess
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.engine import URL
from sqlalchemy import text
from pathlib import Path


@pytest.fixture(scope="session")
def test_db_session():
    print("start of db session fixture")
    db_url = URL.create(
    drivername="postgresql",
    username="service_app_admin",
    host="localhost",
    password="adminPassw0rd1",
    database="work_services_test")
    
    
    engine = create_engine(db_url, echo=True) 
    connection = engine.connect()
    session = Session(bind=engine.connect())
    
    test_sql = text("select count(*) from work_order")
    rs = connection.execute(test_sql)
    id_count = rs.first()[0]
    assert id_count > 1
    return session
   
