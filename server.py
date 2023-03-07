"""Server for melon tasting scheduler app."""

import os

from flask import (Flask, render_template, request, flash, session, redirect)

from model import connect_to_db, db

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

    user = request.form.get("login")

if __name__ == "__main__":
    connect_to_db(app)

    app.secret_key = os.environ['SECRETKEY']
    app.run(host="0.0.0.0", debug=True)
