"""Crud operations"""

from model import db, User, connect_to_db

from datetime import datetime, timedelta

def create_user(name):
    """Creates and returns a user"""

    user = User(user_name = name)

    return user

def login_user(user_name):
    """Logs in user"""

    user = User.query.filter(User.user_name == user_name).first()

    if user:
        return user
    else:
        return False
    

if __name__ == '__main__':
    from server import app
    connect_to_db(app)