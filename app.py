from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
from routes import *
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recommendations.sqlite3'
app.config['SECRET_KEY'] = "random string"


db = SQLAlchemy(app)
#student is for the contact form
class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200)) 
   pin = db.Column(db.String(500))

   def __init__(self, name, city, addr,pin):
      self.name = name
      self.city = city
      self.addr = addr
      self.pin = pin


if __name__ == '__main__':
    db.create_all()
    app.debug = True
    port = int(os.getenv('PORT', 8081))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)