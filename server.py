"""Server for melon tasting scheduler app."""

import os

from flask import (Flask, render_template, request, flash, session, redirect)

from model import connect_to_db, db

import crud

from datetime import datetime, timedelta

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

    name = request.form.get("user_name")
 
    user = crud.login_user(name)

    if user:
        session["login"] = user.user_name

        return render_template('tastings.html', user_name=name)

    else:
        flash("That user does not exist, pleast try again")
        
        return redirect('/')
    
@app.route('/schedule')
def schedule():
    """Schedules a tasting"""

    date = request.args.get("tasting_date")
    start_time = request.args.get("tasting_start")
    end_time = request.args.get("tasting_end")

    user_name = session["login"]

    find_tasting = crud.find_tasting(date, start_time, end_time)

    if find_tasting == False:

        # temp to confirm that form submission working correctly
        flash(f"this time unavailable {date}, {start_time}, {end_time}")

    else:
        # temp to confirm that form submission working correctly
        flash(f"you've selected {date}, {start_time}, {end_time}")

        # populate all available time slots on given day

    return render_template('tastings.html', user_name=user_name)

# TO DO
# populate available tastings
# route to show user's scheduled tastings
# log-out route

if __name__ == "__main__":
    connect_to_db(app)

    app.secret_key = os.environ['SECRETKEY']
    app.run(host="0.0.0.0", debug=True)
