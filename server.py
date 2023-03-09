"""Server for melon tasting scheduler app."""

import os

from flask import (Flask, render_template, request, flash, session, redirect)

from model import connect_to_db, db

import crud

from jinja2 import StrictUndefined

app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined

app = Flask(__name__)

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/login', methods=["POST"])
def login():
    """Logs in user"""

    user_name = request.form.get("login")

    user = crud.login_user(user_name)

    if user == False:
        flash("That user does not exist, pleast try again")
        return redirect('/')

    else:

        session["login"] = user.user_name

        return render_template('tastings.html', user_name=user_name)



if __name__ == "__main__":
    connect_to_db(app)

    app.secret_key = os.environ['SECRETKEY']
    app.run(host="0.0.0.0", debug=True)
