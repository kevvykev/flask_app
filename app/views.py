"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, jsonify
from app.models import UserSchema
from app.models import User
from app import db
import time
from . forms import profile_form
import random
import json
#from app.models import UserSchema

'''Function declaration'''
def timeinfo():
  now = time.strftime("%a, %b %d 20%y")
  return now


###
# Routing for your application.
###
@app.route('/theform',methods=["GET","POST"])

def theform():
  form = profile_form()
  if request.method == 'POST':
    userid = randint('000000000,99999999')
    #pic = 'octocat.png'
    new_user = User(userid,form.firstname.data,form.lastname.data,form.age.data,form.sex.data)
    db.session.add(new_user)
    db.session.commit()
  return render_template('profileform.html', form=form)

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/_get_current_user')
def get_current_user():
  username = "bob"
  email = "bob@example.com"
  id = "3424324"
  return jsonify(username=username,
                   email=email,
                   id=id)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

@app.route("/profiles/",methods=["POST", "GET"])
def profiles():
  '''render webpage profiles'''
  users = db.session.query(User).all()
  serializer = UserSchema(many=True)
  result = serializer.dump(users)
  return jsonify({'Users':result.data})


@app.route("/profile<userid>/", methods=["GET"])
def user(userid):
  users = db.session.query(User).first()
  return users.firstname



if __name__ == '__main__':
  app.run(debug=True, host=os.getenv("IP", '0.0.0.0'),port=int(os.getenv("PORT", 8080) ))