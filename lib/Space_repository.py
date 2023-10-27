from lib.Space import Space
import json
from datetime import date, timedelta, datetime

class Space_repository():
    def __init__(self, connection):
        self._connection = connection

    def all_spaces(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = [Space(
            row['id'],
            row['name'],
            row['description'],
            row['price'],
            row['availability_from'],
            row['availability_till'],
            row['calendar'],
            row['user_id']
            ) for row in rows]

        return spaces

    def add_space(self, space_object):
        if space_object.is_valid() == True:
            self._connection.execute("INSERT INTO spaces (name, description, price, availability_from, availability_till, calendar, user_id) "\
                                    "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                    [space_object.name, space_object.description, space_object.price, space_object.availability_from, space_object.availability_till, space_object.calendar, space_object.user_id])
        
    def search_by_id(self, space_id):
        rows = self._connection.execute("SELECT * FROM spaces WHERE id=%s", [space_id])
        row = rows[0]
        return Space(
            row['id'],
            row['name'],
            row['description'],
            row['price'],
            row['availability_from'],
            row['availability_till'],
            row['calendar'],
            row['user_id']
            )
    
    # renders list of html options for dropdown menu to list in template
    # all unavailable dates are greyed out
    def get_dates_by_id(self, space_id):
        space = self.search_by_id(space_id)

        # turn calendar dict string into dict
        calendar = json.loads(space.calendar)

        calendar_html = []
        for key, value in calendar.items():
            if value == True:
                calendar_html.append(f'<option value="{key}">{key}</option>')
            if value == False:
                calendar_html.append(f'<option value="{key}">not available</option>')
        return calendar_html

    def get_calendar_from_dates(self, start_date, end_date):
        start_date_object = start_date.date()
        end_date_object = end_date.date()
        date_list = []

        # iterate through all dates between start and end to append to list of dates
        current_date_object = start_date_object
        while current_date_object <= end_date_object:
            date_list.append(current_date_object.strftime("%d/%m/%y"))
            current_date_object += timedelta(days=1)
        
        # create dictionary and set values as True by default
        calendar = {date:True for date in date_list}
        calendar_string = str(calendar).replace('\'', "\"").replace(": ", ":").replace("T", "t")
        return calendar_string
        
    
    def search_by_user_id(self, user_id):
        rows = self._connection.execute("SELECT * FROM spaces WHERE user_id=%s", [user_id])
        spaces = [Space(
            row['id'],
            row['name'],
            row['description'],
            row['price'],
            row['availability_from'],
            row['availability_till'],
            row['calendar'],
            row['user_id']
            ) for row in rows]
        return spaces