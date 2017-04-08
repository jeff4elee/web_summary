from flask import render_template, flash, redirect, session, url_for, request, g
from home import app, db, login_manager
from scraper import WScraper 
from .forms import URLForm
from .models import User

@app.route('/', methods=['Post'])
@app.route('/index', methods=['Post'])
def index():

	return mongo
	form = URLForm()

	if form.validate_on_submit():

		try:

			scraper = WScraper()

			scraper.access_page(form.url.data)

			return scraper.render()

		except:

			return "Woops"

	return render_template('index.html',
							form=form)

	

