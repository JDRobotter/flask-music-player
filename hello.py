#!/usr/bin/env python

import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment,Bundle

# app
app = Flask(__name__)

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)

  def __init__(self, username, email):
    self.username = username
    self.email = email

  def __repr__(self):
    return '<User %s>'%self.username

# Assets
assets = Environment(app)
js = Bundle('js/jquery-3.2.1.min.js','js/main.js',
              output='bundle.js')
assets.register('js_all',js)

css = Bundle('css/normalize.css','css/skeleton.css','css/style.css',
              output='bundle.css')
assets.register('css_all',css)

# Rules

@app.route('/img/<path:path>')
def send_img(path):
  return flask.send_from_directory('static/img',path)


@app.route('/install')
def show_install():
  db.create_all()
  return ''

@app.route('/')
def show_index():

  import glob,os
  imgs = glob.glob('static/img/covers/*.jpg')
  allimgs = [os.path.split(img)[-1] for img in imgs]
  objs={
    'albums': allimgs,
  }
  return flask.render_template('index.html',objs=objs)

