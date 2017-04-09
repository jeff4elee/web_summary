import requests
import re
from bs4 import BeautifulSoup

class Analyzer():

	def __init__(self, url):
		self._statistics = {}
		self._scraper = WScraper()
		self._scraper.access_page(url)

	def set_url(self, url):
		self._scraper.access_page(url)

	def count_tags(self, properties=None):

		result = self._scraper.apply_filter(properties).access_properties()

		return str(len(result))


class WScraper():

	def __init__(self, soup=None, pages=None, filters=None):
		self._soup = soup
		self._pages = pages if pages else []
		self._filters = filters if filters else []

	def access_page(self, url):
		""" 
			access_page(url)
				url -> url string of the page to scrape

			Sets up bs4 to target url
		"""

		page = requests.get(url)
		self._soup = BeautifulSoup(page.content, 'html.parser')

	def apply_filter(self, properties):
		""" 
			apply_filter(properties)
				properties -> list of elements to include/filter by

			Returns a modified version of the webscraper where it applies
			operations through a filter
		"""

		self._filters = properties

		return WScraper(self._soup, self._pages, self._filters)

	def access_properties(self):

		if not self._filters:
			return self._soup.find_all(text=True)

		concat_result = self._soup.find_all(self._filters[0])

		# append all ResultSets included in the filter and scraped by the soup
		for i in range(1, len(self._filters)):

			concat_result += self._soup.find_all(self._filters[i])

		return concat_result

	def render(self):
		""" 
			render()

			Returns the html of the page the webscraper is currently accessing
		"""

		if not self._filters:
			return self._soup.prettify()

		# assign concat_result to the first ResultSet scraped by the soup
		# through a filter
		concat_result = self._soup.find_all(self._filters[0])


		# append all ResultSets included in the filter and scraped by the soup
		for i in range(1, len(self._filters)):

			concat_result += self._soup.find_all(self._filters[i])

		return ''.join(str(concat_result).split('n'))

	def render_text(self):
		""" 
			render_text()

			Returns the text of the page the webscraper is currently accessing
		"""

		# prevents scripts/comments and the like from showing up in the text
		# only accepts "visible" portions of the website
		def visible(element):
			if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
				return False
			elif re.match('<!--.*-->', unicode(element)):
				return False
			return True

		if not self._filters:

			# retrieve all the text on the website
			texts = self._soup.find_all(text=True)

			# return the texts that are non comments
			return '<br>'.join(filter(visible, texts))

		html_result = ''

		for f in self._filters:

			for node in self._soup.find_all(f):

				texts = node.find_all(text=True)
				html_result += '<br>'.join(filter(visible, texts))

		return html_result