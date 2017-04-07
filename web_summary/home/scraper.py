import requests
import csv
from bs4 import BeautifulSoup

class WScraper():

	def __init__(self):
		self._soup = None
		self._pages = []

	def access_page(self, url):

		page = requests.get(url)
		self.soup = BeautifulSoup(page.content, 'html.parser')
