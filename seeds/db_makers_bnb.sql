
-- DROP SEQUENCE IF EXISTS <table_name>_id_seq;

-- -- Then, we recreate them
-- CREATE SEQUENCE IF NOT EXISTS <table_name>_id_seq;
-- CREATE TABLE <table_name> (
--     id SERIAL PRIMARY KEY,
--     <column> text,
--     <column> int,
-- );

-- INSERT INTO <table_name> (<columns>) VALUES (<values>);

DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price int,
    availability_from text,
    availability_till text,
    calendar text,
    user_id int
);
-- Listing 1: Cozy Cottage Retreat

INSERT INTO spaces (name, description, price, availability_from, availability_till, calendar, user_id)
VALUES (
    'Cozy Cottage Retreat',
    'Escape to this charming cottage for a tranquil retreat. Nestled in the heart of nature, this cozy cottage offers a serene getaway, perfect for nature lovers and those seeking relaxation.',
    120,
    '10/11/22',
    '23/22/22',
    '{"10/11/22":true,"11/11/22":true,"12/11/22":true,"13/11/22":true,"14/11/22":true,"15/11/22":true,"16/11/22":true,"17/11/22":true,"18/11/22":true,"19/11/22":true,"20/11/22":true,"21/11/22":true,"22/11/22":true,"23/11/22":true}',
    3
);

-- Listing 2: Modern Urban Loft
INSERT INTO spaces (name, description, price, availability_from, availability_till, calendar, user_id)
VALUES (
    'Modern Urban Loft',
    'Experience city living at its finest in this stylish urban loft. With modern amenities and a prime downtown location, this loft is ideal for urban explorers and business travelers.',
    200,
    '15/11/22',
    '01/12/22',
    '{"15/11/22":true, "16/11/22":true, "17/11/22":true, "18/11/22":true, "19/11/22":true, "20/11/22":true, "21/11/22":true, "22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true}',
    1
);

-- Listing 3: Beachfront Paradise
INSERT INTO spaces (name, description, price, availability_from, availability_till, calendar, user_id)
VALUES (
    'Beachfront Paradise',
    'Wake up to the sound of waves in this beachfront paradise. Enjoy direct beach access, stunning ocean views, and a serene atmosphere, making it a dream vacation spot for beach enthusiasts.',
    300,
    '22/11/22',
    '05/01/23',
    '{"22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true, "27/11/22":true, "28/11/22":true, "29/11/22":true, "30/11/22":true, "01/12/22":true, "02/12/22":true, "03/12/22":true, "04/12/22":true, "05/12/22":true, "06/12/22":true, "07/12/22":true, "08/12/22":true, "09/12/22":true, "10/12/22":true, "11/12/22":true, "12/12/22":true}',
    2
);

DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    name text,
    email text,
    password text
);

INSERT INTO users (username, name, email, password) VALUES ('Amina_1', 'Amina', 'Amina@mail.com','Amina123!');
INSERT INTO users (username, name, email, password) VALUES ('Jake_1', 'Jake', 'Jake@mail.com','Jake123!');
INSERT INTO users (username, name, email, password) VALUES ('Sudhansh_1', 'Sudhansh', 'Sudhansh@mail.com','Sudhansh123!');

-- ### request tables over
-- REQUEST TAABLES #############

DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS requests_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS requests_id_seq;
CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    request_user_id int,
    space_id int,
    requested_date text,
    status boolean
);

-- request 1 
INSERT INTO requests (request_user_id, space_id, requested_date, status) 
VALUES (1,3, '12/12/23',FALSE);

-- request 2 
INSERT INTO requests (request_user_id, space_id, requested_date, status) 
VALUES (2,2,'03/08/23',FALSE);


-- ### request tables over



