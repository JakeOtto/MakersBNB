from lib.request import *

# test class constructor 
def test_constructor():

    #creating instance of request class with set data
    new_request = Request( None, 2, 1, "13/2/23", False)
    assert new_request.id == None
    assert new_request.request_user_id == 2
    assert new_request.space_id == 1
    assert new_request.requested_date == "13/2/23"
    assert new_request.status == False

#testing approve request - switching request status to True
def test_approve_request():
    new_request = Request( None, 2, 1, "13/2/23", False)

    new_request.approve_request()
    assert new_request.status == True

# Two equal objects
def test_comparing_two_equal_request_objects():
    new_request_1 = Request( None, 2, 1, "13/2/23", False)
    new_request_2 = Request( None, 2, 1, "13/2/23", False)
    assert new_request_1 == new_request_2

    