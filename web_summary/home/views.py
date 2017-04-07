from flask import render_template, flash, redirect, session, url_for, request, g
from home import app
from scraper import WScraper 

@app.route('/')
@app.route('/index')
def index():

	scraper = WScraper()

	scraper.access_page("https://google.com")

	return scraper.render()