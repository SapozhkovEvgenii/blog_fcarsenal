import requests
from bs4 import BeautifulSoup as BS


class Parse:
    def __init__(self, url):
        self.url = url

    def response(self):
        response = requests.get(self.url)
        page = BS(response.text, 'lxml')
        return page
