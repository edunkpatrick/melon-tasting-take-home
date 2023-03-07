"""Model for melon tasting schedule app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Schedule(db.Model):
    """Schedule"""

    __tablename__ = "schedule"

    schedule_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        """Show info about schedule"""
        return f"<Schedule id={self.schedule_id}"
    
class User(db.Model):
    """User"""

    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        """Show info about user"""
        return f"<User id={self.user_id} name={self.user_name}"


def connect_to_db(flask_app, db_uri="postgresql:///melon_sched_db", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    connect_to_db(app)