"""Crud operations"""

from model import db, User, Tasting, connect_to_db

from datetime import datetime, timedelta

def create_user(name):
    """Creates and returns a user"""

    user = User(user_name = name)

    return user

def login_user(user_name):
    """Returns a user by user_name"""

    return User.query.filter(User.user_name == user_name).first()

def find_tasting(tasting_date, start_time, end_time):
    """Find an available a tasting"""

    is_available = Tasting.query.filter(Tasting.tasting_date == tasting_date, Tasting.available == True).all()
    
    if is_available:
        # need to populate all available time slots to pass to server.py
        return True
    
    else:
        return False

# TO DO
# function to select appointment time
# function to show scheduled tastings for user


if __name__ == '__main__':
    from server import app
    connect_to_db(app)