from functools import wraps
from flask import session, render_template

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            return render_template('access_denied.html')
    return decorated_view