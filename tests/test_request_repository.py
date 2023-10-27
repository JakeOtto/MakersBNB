from lib.request_repository import *
from lib.request import *

def test_request_add(db_connection):

    db_connection.seed("seeds/db_makers_bnb.sql")   #seed db for tests
    new_repo = Request_repository(db_connection)    #Create a repository instance
    new_request = Request(None, 2, 1, "13/2/23", False)  # Create a new request instance
    new_repo.add_request(new_request)  # Pass the request instance to the add_request method

    assert new_request.id == None
    assert new_request.request_user_id == 2
    assert new_request.space_id == 1
    assert new_request.requested_date == "13/2/23"
    assert new_request.status == False


def test_get_all_requests(db_connection):
    
    db_connection.seed("seeds/db_makers_bnb.sql")       #seeding db
    new_repository = Request_repository(db_connection)  #repository instance
    
    all_requests = new_repository.get_all_requests()            #expected result 
    assert all_requests == [Request(1, 1,2, '12/12/23',False), \
                            Request(2, 2,3,'03/08/23',False)]
    

def test_get_request_for_user(db_connection):

    db_connection.seed("seeds/db_makers_bnb.sql")       #seeding db
    new_repository = Request_repository(db_connection)  #repository instance
    
    assert new_repository.get_requests_for_user(2) == [Request(2,2,3,'03/08/23',False)]