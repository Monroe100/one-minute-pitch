from flask import render_template,redirect,url_for,abort
from . import main

@main.route('/')
def index():
    return '<h1> pitches </h1>'

