import flask
from flask import Flask
from flask import render_template

import db
import db2
app = flask.Flask(__name__)

import sqlite3
conn = sqlite3.connect('app.db')


@app.route("/")
def enter():
  return render_template('index.html')

@app.route('/registraion')
def registration():
  return render_template('registr.html')

@app.route('/sign_in')
def sign_in():
  return render_template('sign in.html')

@app.route('/search_page')
def search():
  return render_template('mainpage.html')

@app.route('/helping')
def helping():
  return render_template('help.html')

@app.route('/help_outcome')
def help_outcome():
  return "your response sent :)"

@app.route('/request/<requestname>')
def show_user_request(requestname):
  requestname= db.get_request(requestname)
  return render_template('show_user_request.html', requestname=requestname)


@app.route('/you_took_help')
def you_took_help():
  return "you_took_help :)"

@app.route('/add_request')
def add_request():
  return render_template('addrequest.html')

@app.route('/you_publish_request')
def publish_request():
  return "Congratulations! You publish request! :)"

@app.route('/user/<username>')
def userpage(username):
  username = db2.get_user(username),
  return render_template('userpage.html', username = username)






#seminar 20 nov

@app.route('/search')
def search_for_person():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()

    q = flask.request.args.get('query')

    requests = db.get_requests_by_name(q)

    c.execute("SELECT * FROM request WHERE name LIKE '%s'" % q)
    users = list(c.fetchall())

    c.close()
    return render_template('search_results.html', q=q, requests=requests)

@app.route('/search_page1')
def search1():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()

    q = ""

    c.execute("SELECT * FROM staff WHERE name LIKE '%s'" % q)
    users = list(c.fetchall())

    c.close()
    return render_template('page1.html', users=users)

app.run()