from myresume import db
from datetime import datetime

class Author(db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.INTEGER)
    phone = db.Column(db.INTEGER)
    bio = db.Column(db.String)

class Ability(db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    name = db.Column(db.String)
    body = db.Column(db.String)


class Expextation(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String)
    body = db.Column(db.String)


class Comment(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    author = db.Column(db.String)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow())
