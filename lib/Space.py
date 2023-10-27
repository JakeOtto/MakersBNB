## Space
# Properties:
# - self.id - INT
# - self.name - STRING
# - self.description - STRING
# - self.price - FLOAT
# - self.availability_from - STRING
# - self.availability_till - STRING
# - self.calendar - DICT (date:boolean)

class Space(): 
    def __init__(self, id, name, description, price, availability_from, availability_till, calendar, user_id):
        self.id = id
        self.name = name
        self. description = description
        self.price = price
        self.availability_from = availability_from
        self.availability_till = availability_till
        self.calendar = calendar
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nPrice: {self.price}\nAvailable: {self.availability_from} - {self.availability_till}\nDates: {self.calendar}"

    def is_valid(self):
        if (self.name == "") or (self.description == "") or (self.price == "") or (self.availability_from == "") or (self.availability_till == "") or\
        (self.name == None) or (self.description == None) or (self.price == None) or (self.availability_from == None) or (self.availability_till == None):
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if (self.name == "") or (self.description == "") or (self.price == "") or (self.availability_from == "") or (self.availability_till == "") or\
        (self.name == None) or (self.description == None) or (self.price == None) or (self.availability_from == None) or (self.availability_till == None):
            errors.append("Form is not complete. Try again!")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)