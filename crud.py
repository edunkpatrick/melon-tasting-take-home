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

def create_tasting(user_name, tasting_date, tasting_time):
    """Create and return a tasting"""

    name = User.query.filter(User.user_name == user_name).first()
    user_id = name.user_id

    tasting = Tasting(tasting_date=tasting_date, tasting_time=tasting_time, 
                      user_id=user_id, available = False)

    return tasting

if __name__ == '__main__':
    from server import app
    connect_to_db(app)