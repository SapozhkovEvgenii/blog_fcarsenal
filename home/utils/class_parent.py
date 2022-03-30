import requests
from bs4 import BeautifulSoup as BS
from time import sleep

class Parse:
    def __init__(self, url):
        self.url = url

    def response(self):
        response = requests.get(self.url)
        sleep(1)
        page = BS(response.text, 'lxml')
        return page
