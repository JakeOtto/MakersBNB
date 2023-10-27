from lib.Space import Space

def test_init():
    test_space = Space(
        None,
        "test name",
        "test description",
        666,
        "test availability_from",
        "test avaiability_till",
        "{test:calendar}",
        1
        )
    assert test_space.name == "test name"
    assert test_space.description == "test description"
    assert test_space.price == 666
    assert test_space.availability_from == "test availability_from"
    assert test_space.availability_till == "test avaiability_till"
    assert test_space.calendar == "{test:calendar}"
    assert test_space.user_id == 1

def test_eq():
    test_space = Space(
        None,
        "test name",
        "test description",
        666,
        "test availability_from",
        "test avaiability_till",
        "{test:calendar}",
        2
        )
    test_space1 = Space(
        None,
        "test name",
        "test description",
        666,
        "test availability_from",
        "test avaiability_till",
        "{test:calendar}",
        2
        )
    assert test_space == test_space1
