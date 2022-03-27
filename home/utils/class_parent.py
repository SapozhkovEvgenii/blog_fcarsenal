import requests
from bs4 import BeautifulSoup as BS


class Parse:
    def __init__(self, url, selector):
        self.url = url
        self.selector = selector

    def response(self):
        response = requests.get(self.url)
        page = BS(response.text, features="html.parser")
        text = page.select(self.selector)
        return text
