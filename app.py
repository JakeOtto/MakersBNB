import os
from flask import Flask, request, render_template, redirect, url_for, session, flash
from lib.database_connection import get_flask_database_connection
from lib.Space_repository import Space_repository
from lib.Space import Space
from lib.User_repository import User_repository
from lib.User import User
from lib.request_repository import Request_repository
from lib.request import Request
from lib.Space_repository import Space_repository
from lib.Space import Space
# import custom decorator which authentocates the user
from lib.login_required import login_required
from datetime import datetime, timedelta

# Create a new Flask app
app = Flask(__name__)
# BUG
# Temporary disclosed secret key as env variable doesnt work
app.secret_key = "hdcvfhjw6r86ojkdbkw"

# [GET] /
# Returns the homepage
@app.route('/', methods=['GET'])
def get_homepage():
    return render_template('index.html')

# [GET][POST] /login 
# Returns the login page with login form
# Posts and validates login details to databade
# If login is validated,  creates new session
@app.route('/login', methods=['GET', 'POST'])
def login():
    connection = get_flask_database_connection(app)

    if 'logged_in' in session and session['logged_in']:
        # User is already logged in, redirect them to a different page
        return redirect('/spaces')  
        
    if request.method == 'GET':
        return render_template('login.html')
    
    # Route for processing the login form submission
    if request.method == 'POST':
        # Retrieve login details from the form
        username = request.form.get('username')
        password = request.form.get('password')

        user_repository = User_repository(connection)

        if user_repository.login_valid(username, password) == True:
            user_object = user_repository.get_user_by_username(username)
            # starts a new session
            session['logged_in'] = True
            session['username'] = username
            session['user_id'] = user_object.id
            return redirect('/spaces')
        else:
            errors = True
            return render_template('login.html', errors=errors) 


# [GET][POST] /signup
# Returns the signup page with signup form
# Posts signup details to database
@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def post_signup():
    connection = get_flask_database_connection(app)
    user_repository = User_repository(connection)

    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    new_user = User(None, username, name, email, password)
    errors = user_repository.generate_errors(new_user)
    # if there are no errors, user is added
    if user_repository.validate_new_user(new_user) == True and errors == []:
        user_repository.add_user(new_user)
        message = "Thank you, you are signed up! Now login."
        return render_template('signup.html', message=message)
    # if there are errors, we print them
    else:
        return render_template('signup.html', errors=errors)

# [GET] /spaces -- template = spaces
# Returns page with all spaces listed
# @app.route('/spaces', methods=['GET'])
@app.route('/spaces', methods = ['GET'])
@login_required
def spaces_list():
    connection = get_flask_database_connection(app)
    space_repository = Space_repository(connection)
    lst = space_repository.all_spaces()
    return render_template('spaces.html', spaces =lst)

# [GET][POST] /spaces/new -- template = new_place.html
# Returns page with all spaces listed
# Posts a new space listing
# @app.route('/spaces/new', methods=['GET'])
# @app.route('/spaces/new', methods=['POST'])

@app.route('/spaces/new', methods = ['GET', 'POST'])
@login_required
def new_space():
    connection = get_flask_database_connection(app)
    repository = Space_repository(connection)
    if request.method == 'GET':
        space_repository = Space_repository(connection)
        lst = space_repository.all_spaces()

        # passing minimum date to choose as today
        # maximum date to choose as in a year
        min_date = datetime.now().strftime('%Y-%m-%d')
        max_date = (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d')

        return render_template('new_space.html', spaces =lst, min_date=min_date, max_date=max_date)
    elif request.method == 'POST':

        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        user_id = session.get('user_id')

        available_from = request.form['available_from']
        available_from = datetime.strptime(available_from, '%Y-%m-%d')
        available_till = request.form['available_till']
        available_till = datetime.strptime(available_till, '%Y-%m-%d')
        space_repository = Space_repository(connection)
        calendar = space_repository.get_calendar_from_dates(available_from, available_till)

        new_space = Space(None,name, description, price, available_from, available_till, calendar, user_id)
        if not new_space.is_valid():
            return render_template('/new_space.html', space = new_space, errors = new_space.generate_errors()), 400
        
        else:
            place_price = float(price)
            # get calendar dictionary
            the_place = Space(None,name, description, place_price, available_from, available_till, calendar, user_id)
            repository.add_space(the_place)
            return redirect(f"/spaces")

# [GET] /spaces/<id> -- template = spaces
# Returns page specific space by its' id with calendar to choose a booking date
# This is a page where user post a request
# Posts a new request for booking a space
@app.route('/spaces/<id>', methods=['GET', 'POST'])
@login_required
def get_single_space(id):
    if request.method == 'GET':
        connection = get_flask_database_connection(app)

        # get space object and pass to in jinja args
        space_repository = Space_repository(connection)
        space = space_repository.search_by_id(id)

        # get available dates for the space and display dropdown calendar
        calendar = space_repository.get_dates_by_id(id)

        return render_template('single_space.html', space=space, calendar=calendar)

    if request.method == 'POST':
        connection = get_flask_database_connection(app)
        request_repository = Request_repository(connection)
        requested_date = request.form["booking_date"]
        request_user_id = session.get('user_id')
        space_id = id

        # new_request false by default
        new_request = Request(None, request_user_id, space_id, requested_date, False)
        request_repository.add_request(new_request)
        message = "Thank you for your request!"

        space_repository = Space_repository(connection)
        space = space_repository.search_by_id(id)
        calendar = space_repository.get_dates_by_id(id)
        url = f"/spaces/{id}"

        return render_template('single_space.html', space=space, calendar=calendar, url=url, message=message)

@app.route('/requests', methods=['GET'])
@login_required
def get_user_requests():
    user_id = session.get('user_id')
    print (f"heres method user id - {user_id}")
    connection = get_flask_database_connection(app)
    request_repository = Request_repository(connection)
    requests = request_repository.get_requests_for_user(user_id)

    # get requests done by logged in user (owner)
    space_repository = Space_repository(connection)
    # search for spaces owned by user
    spaces_owned = space_repository.search_by_user_id(user_id)
    # search for spaces id's
    spaces_owned_ids = [space.id for space in spaces_owned]
    # search for requests with that id's
    # if space_id from user owned spaces is in request.space_id this request is appended
    owner_requests = []
    for request in request_repository.get_all_requests():
        if request.space_id in spaces_owned_ids:
            owner_requests.append(request)

    # get space id and retrieve space name, pass psace repo
    return render_template('request.html', owner_requests=owner_requests, requests=requests, space_repo=Space_repository(connection))

#Redirects to relevant request page
@app.route('/load_request', methods=['POST'])
@login_required
def load_request():
    id = request.form['request_id']
    return redirect(f"/requests/{id}")


@app.route('/load_owner_request', methods=['POST'])
@login_required
def load_owner_request():
    id = request.form['owner_request_id']
    return redirect(f"/requests/{id}")

@app.route('/requests/<id>', methods=['GET'])
@login_required
def get_request_details(id):
    connection = get_flask_database_connection(app)
    connection.connect()

    user_repo = User_repository(connection)
    user = user_repo.get_user_by_username(session.get("username"))

    request_repo = Request_repository(connection)
    # id_one_up = str(int(id) + 1)
    #BUG id -> user id not request user
    request = request_repo.get_request_by_id(id)
    requests = request_repo.get_all_requests()
    request_user = user_repo.get_user_by_id(request.request_user_id)
    print(f"USER SHLOUD BE AMINA:{request_user.username}")

    space_repo = Space_repository(connection)
    space = space_repo.search_by_id(request.space_id)

    return render_template('request_details.html', user=user, request_user=request_user, request=request, requests=requests, space=space)

@app.route('/request_response', methods=['POST'])
@login_required
def update_request_status():
    connection = get_flask_database_connection(app)
    connection.connect()

    response = request.form['action'].split('-')
    id = response[0]
    response_type = response[1]

    request_repo = Request_repository(connection)
    if (response_type == 'cancel'):
        request_repo.delete_request(id)
    else:
        request_repo.toggle_status(id)
       

    return redirect("/requests")

    



@app.route('/logout')
def logout():
    # Clear the session data to log the user out
    session.clear()
    return redirect('/login')
  

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
    # app.secret_key = os.environ.get("SECRET_KEY_SESSION")
