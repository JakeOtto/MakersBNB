from lib.request import *

class Request_repository:
    
    # setup connection
    def __init__(self,connection):
        self._connection = connection

    # adding a request, taking a request object
    def add_request(self, request):

        self._connection.execute('INSERT INTO requests (request_user_id, space_id, requested_date, status) VALUES (%s, %s, %s, %s)', [
                                request.request_user_id, request.space_id, request.requested_date, request.status])
        return None

    # getting list of all requests
    def get_all_requests(self):
        rows = self._connection.execute('SELECT id, request_user_id, space_id, requested_date, status from requests')
        requests = []
        for row in rows:
                    # setting requests with the 5 variables
            item = Request( row["id"], row["request_user_id"], row["space_id"], row["requested_date"], row["status"])
            requests.append(item)
        return requests

    # Retrieve requests associated with a specific space ID
    def get_requests_for_space(self, space_id):
        rows = self._connection.execute(
            'SELECT id, request_user_id, space_id, requested_date, status FROM requests WHERE space_id = %s', [space_id]
        )
        requests = []
        for row in rows:
            item = Request(row["id"], row["request_user_id"], row["space_id"], row["requested_date"], row["status"])
            requests.append(item)
        return requests
    

    # Retrieve requests associated with a specific user ID
    def get_requests_for_user(self, user_id):
        rows = self._connection.execute(
            'SELECT id, request_user_id, space_id, requested_date, status FROM requests WHERE request_user_id = %s',
            [user_id]
        )
        requests = []
        for row in rows:
            item = Request(row["id"], row["request_user_id"], row["space_id"], row["requested_date"], row["status"])
            requests.append(item)
        return requests
    
    def get_request_by_id(self, request_id):
        rows = self._connection.execute(
            'SELECT id, request_user_id, space_id, requested_date, status FROM requests WHERE id = %s',
            [request_id]
            )
        row = rows[0]
        return Request(row["id"], row["request_user_id"], row["space_id"], row["requested_date"], row["status"])
        
    def toggle_status(self, request_id):
        request = self.get_request_by_id(request_id)
        self._connection.execute('UPDATE requests SET status = %s WHERE id = %s', [not request.status, request_id])
        return None
    
    def delete_request(self, request_id): #Need to add foreign keys eventually to SQL schema
        self._connection.execute('DELETE from requests WHERE id = %s', [request_id])
        return None
