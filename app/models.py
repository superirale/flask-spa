from datetime import datetime
from app import db

class Contact(db.Model):
    "SQLAlchemy contact model"
    __tablename__ = "contacts"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(255))
    email = db.Column('email', db.String(120), unique=True)
    phone = db.Column('phone', db.String(120))
    added_on = db.Column('added_on', db.DateTime)
    
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.added_on = datetime.utcnow()

    def __repr__(self):
        return '<Contact %r>' % self.name
