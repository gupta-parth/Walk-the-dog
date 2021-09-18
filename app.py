from flask import Flask
from flask import flash, redirect, render_template, session, request, jsonify, make_response, url_for
from functools import wraps

from werkzeug.exceptions import MethodNotAllowed

app = Flask(__name__)

def login_required(f):
    """
    Decorate routes to require login.
    
    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    return render_template("index.html")
