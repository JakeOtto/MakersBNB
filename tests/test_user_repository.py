from lib.User_repository import User_repository
from lib.User import User
"""
+ method(type): type
add_user : 
login_valid :
"""
"""
Users list
"""
def test_get_all_users(db_connection):
    db_connection.seed("seeds/db_makers_bnb.sql")
    repository = User_repository(db_connection)

    users=repository.all()
    assert users == [User(1,'Amina_1', 'Amina', 'Amina@mail.com','Amina123!'), \
                    User(2, 'Jake_1', 'Jake', 'Jake@mail.com','Jake123!'), \
                    User(3, 'Sudhansh_1', 'Sudhansh', 'Sudhansh@mail.com','Sudhansh123!')]

"""
Add a new user 
"""
def test_add_new_user(db_connection):
    db_connection.seed("seeds/db_makers_bnb.sql")
    repository = User_repository(db_connection)

    repository.add_user(User(4, "Gin_71", "Gina", "gina@mail.com", "Gina123!"))
    users = repository.all()
    assert users == [User(1,'Amina_1', 'Amina', 'Amina@mail.com','Amina123!'), \
                    User(2, 'Jake_1', 'Jake', 'Jake@mail.com','Jake123!'), \
                    User(3, 'Sudhansh_1', 'Sudhansh', 'Sudhansh@mail.com','Sudhansh123!'), \
                    User(4, "Gin_71", "Gina", "gina@mail.com", "Gina123!")] 

    
"""
Loging a valid user 
"""

def test_login_valid_user(db_connection):
    db_connection.seed("seeds/db_makers_bnb.sql")
    repository = User_repository(db_connection)

    username_to_log = 'Sudhansh_1'
    password_to_log = 'Sudhansh123!'
    
    user_to_log = repository.login_valid(username_to_log, password_to_log)

    assert user_to_log == True

"""
Loging a invalid user with invalid password
"""
def test_login_invalid_password(db_connection):
    db_connection.seed("seeds/db_makers_bnb.sql")
    repository = User_repository(db_connection)

    username_to_log = 'Sudhansh_1'
    password_to_log = 'Sudhansh456!'
    
    user_to_log = repository.login_valid(username_to_log, password_to_log)

    assert user_to_log == False

"""
Loging a invalid user with invalid username
"""
def test_login_invalid_user(db_connection):
    db_connection.seed("seeds/db_makers_bnb.sql")
    repository = User_repository(db_connection)

    username_to_log = 'Sudhansh_11'
    password_to_log = 'Sudhansh123!'
    
    user_to_log = repository.login_valid(username_to_log, password_to_log)

    assert user_to_log == False

"""
Gets user object by user id
"""
def test_get_user_id_by_username(db_connection):
    db_connection.seed("seeds/db_makers_bnb.sql")
    repository = User_repository(db_connection)
    assert repository.get_user_by_username("Amina_1") == User(1,'Amina_1', 'Amina', 'Amina@mail.com','Amina123!')

