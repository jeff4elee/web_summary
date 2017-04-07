from flask import render_template, flash, redirect, session, url_for, request, g
from . import app

@app.route('/')
@app.route('/index')
def index():

	return "Hello"