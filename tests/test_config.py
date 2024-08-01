#from conftest import test_session

def test_setup():
    print(" just ran empty test")
    
def testDBConfig(test_db_session):
    print("Start of db session test")
    assert test_db_session is not None
    