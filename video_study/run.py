#!flask/bin/python

def prep_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

from app import app
from app import db
prep_db()
app.run(debug=True)