from . import home
from flask import Flask, render_template

@home.route('/')
def index():
    return "homepage Of Internship"


@home.route('/free-python')
def python_page():
    return render_template('index.html')