"""Script to seed database"""

import os

# will need datetime to seed tastings table
from datetime import datetime
from datetime import date

import crud
import model
import server

os.system("dropdb melon_db")
os.system("createdb melon_db")

model.connect_to_db(server.app)
model.db.create_all()

for n in range(1, 11):
    name = f"user{n}"

    new_user = crud.create_user(name)
    model.db.session.add(new_user)

    # TO DO
    # seed db with tasting time slots

model.db.session.commit()