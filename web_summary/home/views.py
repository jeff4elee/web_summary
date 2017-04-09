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

		#retrieves the request lists of html properties (tags/attributes)
		properties = request.form.getlist("filters")
		specials = request.form.getlist("specials")

		#instantiates an anaylzer for the given url (calculates statistics)
		analyzer = Analyzer(form.url.data)

		if "render_html" in request.form:
			return analyzer.get_scraper().render_text()

######################################################################################################


		#TODO
		#Don't Repeat Yourself (DRY)
		#Separate the code into methods (perhaps a formatter class)
		#add more statistic anaylsis

		#IDEAS
		#Store previous scraped sites into database for calculations of mean/median/mode
		#Deteremine any correlation between scraped data and other info (who knows what'll come up)
		#idk what else bro

		num_tags = analyzer.count_tags(properties)

		if properties:
			formatted = '<strong>Total number of %s: </strong>' % ' '.join(properties) + str(num_tags)
		else:
			formatted = '<strong>Total number of tags: </strong>' + str(num_tags)

		for p in properties:
			num_tags = analyzer.count_tags([p])
			formatted += '<br><strong>Total number of %s: </strong>' % p[0] + str(num_tags)


		if "href" in specials:
			link_count = analyzer.count_links(outside=True)
			links = analyzer.get_scraper().capture_links(outside=True)

			formatted += '<br><strong>Number of links to outside sites: </strong>' + \
						str(link_count) + '<br>' + \
						'<br>'.join([a['href'] for a in links])

#######################################################################################################

		return render_template('index.html',
								form=form,
								result=formatted)

	return render_template('index.html',
							form=form)