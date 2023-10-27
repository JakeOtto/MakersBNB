from lib.database_connection import DatabaseConnection
from lib.Space_repository import Space_repository
from lib.Space import Space
from datetime import datetime 

"""
When I call all_spaces() method
all spaces are showing
"""
def test_all_spaces(db_connection):
    db_connection.seed('seeds/db_makers_bnb.sql')
    repository = Space_repository(db_connection)

    assert repository.all_spaces() == [ 
        Space(
        1,
        'Cozy Cottage Retreat',
        'Escape to this charming cottage for a tranquil retreat. Nestled in the heart of nature, this cozy cottage offers a serene getaway, perfect for nature lovers and those seeking relaxation.',
        120,
        '10/11/22',
        '23/22/22',
        '{"10/11/22":true,"11/11/22":true,"12/11/22":true,"13/11/22":true,"14/11/22":true,"15/11/22":true,"16/11/22":true,"17/11/22":true,"18/11/22":true,"19/11/22":true,"20/11/22":true,"21/11/22":true,"22/11/22":true,"23/11/22":true}',
        3
        ),
        Space(
            2,
            'Modern Urban Loft',
            'Experience city living at its finest in this stylish urban loft. With modern amenities and a prime downtown location, this loft is ideal for urban explorers and business travelers.',
            200,
            '15/11/22',
            '01/12/22',
            '{"15/11/22":true, "16/11/22":true, "17/11/22":true, "18/11/22":true, "19/11/22":true, "20/11/22":true, "21/11/22":true, "22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true}',
            1
        ),
        Space(
            3,
            'Beachfront Paradise',
            'Wake up to the sound of waves in this beachfront paradise. Enjoy direct beach access, stunning ocean views, and a serene atmosphere, making it a dream vacation spot for beach enthusiasts.',
            300,
            '22/11/22',
            '05/01/23',
            '{"22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true, "27/11/22":true, "28/11/22":true, "29/11/22":true, "30/11/22":true, "01/12/22":true, "02/12/22":true, "03/12/22":true, "04/12/22":true, "05/12/22":true, "06/12/22":true, "07/12/22":true, "08/12/22":true, "09/12/22":true, "10/12/22":true, "11/12/22":true, "12/12/22":true}',
            2
        )
        ]
    

"""
When I call add_space() method
new space is added to database
"""
def test_add_new_space(db_connection):
    repository = Space_repository(db_connection)
    db_connection.seed('seeds/db_makers_bnb.sql')

    test_space = Space(
        None,
        "test name",
        "test description",
        666,
        "test availability_from",
        "test avaiability_till",
        "{test:calendar}",
        3
        )
    repository.add_space(test_space)
    assert repository.all_spaces() == [ 
        Space(
        1,
        'Cozy Cottage Retreat',
        'Escape to this charming cottage for a tranquil retreat. Nestled in the heart of nature, this cozy cottage offers a serene getaway, perfect for nature lovers and those seeking relaxation.',
        120,
        '10/11/22',
        '23/22/22',
        '{"10/11/22":true,"11/11/22":true,"12/11/22":true,"13/11/22":true,"14/11/22":true,"15/11/22":true,"16/11/22":true,"17/11/22":true,"18/11/22":true,"19/11/22":true,"20/11/22":true,"21/11/22":true,"22/11/22":true,"23/11/22":true}',
        3),
        Space(
            2,
            'Modern Urban Loft',
            'Experience city living at its finest in this stylish urban loft. With modern amenities and a prime downtown location, this loft is ideal for urban explorers and business travelers.',
            200,
            '15/11/22',
            '01/12/22',
            '{"15/11/22":true, "16/11/22":true, "17/11/22":true, "18/11/22":true, "19/11/22":true, "20/11/22":true, "21/11/22":true, "22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true}',
            1
        ),
        Space(
            3,
            'Beachfront Paradise',
            'Wake up to the sound of waves in this beachfront paradise. Enjoy direct beach access, stunning ocean views, and a serene atmosphere, making it a dream vacation spot for beach enthusiasts.',
            300,
            '22/11/22',
            '05/01/23',
            '{"22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true, "27/11/22":true, "28/11/22":true, "29/11/22":true, "30/11/22":true, "01/12/22":true, "02/12/22":true, "03/12/22":true, "04/12/22":true, "05/12/22":true, "06/12/22":true, "07/12/22":true, "08/12/22":true, "09/12/22":true, "10/12/22":true, "11/12/22":true, "12/12/22":true}',
            2
        ),
        Space(
            4,
            "test name",
            "test description",
            666,
            "test availability_from",
            "test avaiability_till",
            "{test:calendar}",
            3
            )
            ]

"""
Search for space row by it's id.
"""
def test_search_for_space_by_id(db_connection):
    repository = Space_repository(db_connection)
    db_connection.seed('seeds/db_makers_bnb.sql')

    assert repository.search_by_id(1) == Space(
        1,
        'Cozy Cottage Retreat',
        'Escape to this charming cottage for a tranquil retreat. Nestled in the heart of nature, this cozy cottage offers a serene getaway, perfect for nature lovers and those seeking relaxation.',
        120,
        '10/11/22',
        '23/22/22',
        '{"10/11/22":true,"11/11/22":true,"12/11/22":true,"13/11/22":true,"14/11/22":true,"15/11/22":true,"16/11/22":true,"17/11/22":true,"18/11/22":true,"19/11/22":true,"20/11/22":true,"21/11/22":true,"22/11/22":true,"23/11/22":true}',
        3
        )
"""
When I call add_space() method and not fill all the fields
Then Not added the invalid space
"""
def test_add_invalid_place(db_connection):
    db_connection.seed("seeds/db_makers_bnb.sql")
    repository = Space_repository(db_connection)

    test_space = Space(
        None,
        "test name",
        "test description",
        23,
        "test availability_from",
        "",
        "{test:calendar}",
        3
        )
    
    repository.add_space(test_space)

    assert repository.all_spaces() == [ 
        Space(
        1, 
        'Cozy Cottage Retreat',
        'Escape to this charming cottage for a tranquil retreat. Nestled in the heart of nature, this cozy cottage offers a serene getaway, perfect for nature lovers and those seeking relaxation.',
        120,
        '10/11/22',
        '23/22/22',
        '{"10/11/22":true,"11/11/22":true,"12/11/22":true,"13/11/22":true,"14/11/22":true,"15/11/22":true,"16/11/22":true,"17/11/22":true,"18/11/22":true,"19/11/22":true,"20/11/22":true,"21/11/22":true,"22/11/22":true,"23/11/22":true}',
        3
        ),
        Space(
            2,
            'Modern Urban Loft',
            'Experience city living at its finest in this stylish urban loft. With modern amenities and a prime downtown location, this loft is ideal for urban explorers and business travelers.',
            200,
            '15/11/22',
            '01/12/22',
            '{"15/11/22":true, "16/11/22":true, "17/11/22":true, "18/11/22":true, "19/11/22":true, "20/11/22":true, "21/11/22":true, "22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true}',
            1
            ),
        Space(
            3,
            'Beachfront Paradise',
            'Wake up to the sound of waves in this beachfront paradise. Enjoy direct beach access, stunning ocean views, and a serene atmosphere, making it a dream vacation spot for beach enthusiasts.',
            300,
            '22/11/22',
            '05/01/23',
            '{"22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true, "27/11/22":true, "28/11/22":true, "29/11/22":true, "30/11/22":true, "01/12/22":true, "02/12/22":true, "03/12/22":true, "04/12/22":true, "05/12/22":true, "06/12/22":true, "07/12/22":true, "08/12/22":true, "09/12/22":true, "10/12/22":true, "11/12/22":true, "12/12/22":true}',
            2
        )
        ]


"""
get rendered html dates options by space id
when date is booked displays: not available
"""
def test_get_html_template_options_of_calendar(db_connection):
    repository = Space_repository(db_connection)
    db_connection.seed('seeds/db_makers_bnb.sql')

    test_space = Space(
        None,
        "test name",
        "test description",
        666,
        "test availability_from",
        "test avaiability_till",
        '{"15/11/22":true, "16/11/22":true, "17/11/22":false, "18/11/22":true}',
        2
        )
    repository.add_space(test_space)

    assert repository.get_dates_by_id(4) == [
        '<option value="15/11/22">15/11/22</option>',
        '<option value="16/11/22">16/11/22</option>',
        '<option value="17/11/22">not available</option>',
        '<option value="18/11/22">18/11/22</option>'   
    ]

"""
When I start and end date is inputed
a dictionary calendar is created
"""
def test_dictionary_calendar_created(db_connection):
    repository = Space_repository(db_connection)

    # Create datetime objects for start_date and end_date
    start_date = datetime(2023, 12, 1)
    end_date = datetime(2023, 12, 4)

    assert repository.get_calendar_from_dates(start_date, end_date) == '{"01/12/23":true, "02/12/23":true, "03/12/23":true, "04/12/23":true}'

"""
When I search for id by user_id
I display all spaces which belong to user
"""
def test_get_spaces_by_user_id(db_connection):
    repository = Space_repository(db_connection)
    assert repository.search_by_user_id(1) == [
        Space(
            2,
            'Modern Urban Loft',
            'Experience city living at its finest in this stylish urban loft. With modern amenities and a prime downtown location, this loft is ideal for urban explorers and business travelers.',
            200,
            '15/11/22',
            '01/12/22',
            '{"15/11/22":true, "16/11/22":true, "17/11/22":true, "18/11/22":true, "19/11/22":true, "20/11/22":true, "21/11/22":true, "22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true}',
            1
            )
    ]