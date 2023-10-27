# requests class

class Request:

    def __init__(self, id, request_user_id, space_id, requested_date, status ):
        
        #initialised variables
        self.id =  id
        self.request_user_id = int (request_user_id)
        self.space_id = int (space_id)
        self.requested_date = str (requested_date)
        self.status = bool (status)

    # to set approved 
    def approve_request(self):
        self.status = True

    #for testing equality (to adjust)
    def __eq__(self, other):
        if isinstance(other, Request):
            return (
                self.id == other.id and
                self.request_user_id == other.request_user_id and
                self.space_id == other.space_id and
                self.requested_date == other.requested_date and
                self.status == other.status
            )
        return False

    #for string representation
    def __repr__(self):
        return f"Request({self.id}, requestor's id:{self.request_user_id}, space id:{self.space_id}, requested date:{self.requested_date},current stats:{self.status})"