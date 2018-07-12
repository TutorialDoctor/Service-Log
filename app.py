from flask import Flask, render_template, request, g, redirect, url_for
#from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy 
import sqlite3
from datetime import datetime

#http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.limit

#THIS IS NOT NECESSARY. First, run 'sqlite3 database.db < schema.sql' from the terminal to generate the database.db file from the schema file.

#select * from customer where dateofbirth < date('now','-30 years');

#User.birthday <= '1988-01-17

#from app.py import db. db.create_all()
#2016-01-01 10:20:05.123
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
LIMIT = 30
#Bootstrap(app)

class Services(db.Model):
  __tablename__='services'
  id = db.Column(db.Integer, primary_key=True)
  name =  db.Column(db.String(50))
  date = db.Column(db.DateTime)
  location = db.Column(db.String(50))
  minister = db.Column(db.String(50))
  link = db.Column(db.String(20))
  expiration = db.Column(db.String(50))
  comment = db.Column(db.String(1000))
  assignee_id = db.Column(db.Integer, db.ForeignKey('assignees.id'))

class Assignees(db.Model):
  __tablename__='assignees'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  services = db.relationship('Services', backref='assignee')

@app.route("/")
def index():
  hello_text = "Services"
  result = Services.query.order_by('name desc').limit(LIMIT).all()
  return render_template('index.html', result=result)

@app.route("/enter")
def enter():
  login_text = "You've logged in successfully!"
  return render_template("enter.html",login_text=login_text)

@app.route("/login")
def login():
  login_text = "You've logged in successfully!"
  return render_template("login.html",login_text=login_text)

@app.route('/process', methods=['POST'])
def process():
  name = request.form['name']
  location = request.form['location']
  date = datetime.now()
  minister = request.form['minister']
  link = request.form['link']
  expiration = request.form['expiration']
  comment = request.form['comment']
  assignee = Assignees(name=request.form['assignee'])
  signature = Services(name=name,date=date,location=location,link=link,expiration=expiration,comment=comment,minister=minister,assignee=assignee)
  db.session.add(signature)
  db.session.commit()
  db.session.add(assignee)
  db.session.commit()
  return redirect(url_for('index'))

@app.route('/delete',methods=['DELETE'])
def delete():
  signature = Services(name=name,date=date,location=location,link=link,expiration=expiration,comment=comment,minister=minister)
  db.session.delete(sig)
  db.sessioin.commit
  return redirect(url_for('index'))

  
@app.route('/delete/<int:entry_id>')
def delete_entry(entry_id):
  g.db.execute('delete from entries where id=' + entry_id)

if __name__=='__main__':
  app.run(debug=True)
  