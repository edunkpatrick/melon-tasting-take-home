# Melon Tasting App

Melon Tasting is a Flask app for scheduling 30 min melon tasting appointments.

# Table of Contents

    ⭐ Technologies Used
    ⭐ How to locally run
    ⭐ Features to complete

## Technologies Used

    * Python
    * Flask
    * PostgresSQL
    * SQLAlchemy
    * Jinja
    * HTML

(dependencies are listed in requirements.txt)

## How to locally run

Melon Tasting has not been deployed yet, so follow the instructions below to run the app locally.

### Run the Flask App

    * Set up and activate your python virtualenv
    * Install all dependencies with pip3 install -r requirements.txt
    * Source your secret key from secrets.sh
    * Seed database with python3 seed_db.py
    * Run python3 server.py
    * Go to localhost:5000 to see the webapp

## Features completed
    
    * seeded user db
    * homepage
    * tastings landing page with form to select date, start time, and end time

## Features to complete

    * seed db with tasting time slots
    * function to select appointment time
    * function to show scheduled tastings for user
    * route to populate available tastings within search date/time
    * route to show user's scheduled tastings
    * log-out route
