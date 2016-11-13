#!flask/bin/python

def prep_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

from app import app
from app import db

if __name__ == '__main__':
	prep_db()
	app.run(debug=False)