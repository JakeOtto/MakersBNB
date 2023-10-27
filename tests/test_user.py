from lib.User import User
"""
Initialises 
id: int
username : string
name : string
email : string
password : string
"""

def test_constructor_behabiour():
    new_user = User(1, "username", "name", "email", "password")
    assert new_user.id == 1
    assert new_user.username == "username"
    assert new_user.name == "name"
    assert new_user.email == "email"
    assert new_user.password == "password"


"""
Two equal objects
"""

def test_comparing_two_equal_user_objects():
    new_user_1 = User(1, "username", "name", "email", "password")
    new_user_2 = User(1, "username", "name", "email", "password")
    assert new_user_1 == new_user_2


"""
Format
"""

def test_correct_format():
    new_user = User(1, "username", "name", "email", "password")
    assert str(new_user) == "User id: 1 \nUsername: username, \nName: name, \nEmail: email, \nPassword: password"