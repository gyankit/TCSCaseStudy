from App import db
from datetime import datetime


class User(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    email = db.Column( db.String(120), unique=True, nullable=False )
    username = db.Column( db.String(80), unique=True, nullable=False )
    password = db.Column( db.String(256), nullable=False )
    datetime = db.Column( db.DateTime(timezone=True), nullable=False, default=datetime.utcnow )

    def __init__(self, email, username, password, datetime):  
      self.email = email  
      self.username = username  
      self.password = password  
      self.datetime = datetime  

    def __repr__(self):
        return '<User %r' % self.username

class Customer(db.Model):
    ssnid = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)

    def __init__(self, ssnid, customer_name, age, address, state, city):
      self.ssnid = ssnid
      self.customer_name = customer_name
      self.age = age
      self.address = address
      self.state = state
      self.city = city

    def __repr__(self):
      return '<Customer %r' % self.ssnid