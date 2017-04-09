from flask import render_template, flash, redirect, session, url_for, request, g
from home import app, db, login_manager
from scraper import WScraper, Analyzer
from .forms import URLForm
from .models import User

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

	form = URLForm()

	if form.validate_on_submit():

		properties = request.form.getlist("filters")

		analyzer = Analyzer(form.url.data)
#		scraper = WScraper()

#		scraper.access_page(form.url.data)

		return analyzer.count_tags(properties)
		
		if 'render_text' in request.form:
			return scraper.apply_filter(properties).render_text()

		return scraper.apply_filter(properties).render()


	return render_template('index.html',
							form=form)

	

