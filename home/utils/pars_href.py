import requests
from bs4 import BeautifulSoup as BS

url = "https://fc-arsenal.com/news/all"
hrefs = []

def pars_href():
    response = requests.get(url)
    page = BS(response.text, features="html.parser")
    href_all = page.findAll("div", class_="views-field views-field-title")
    for href in href_all:
        h = "https://fc-arsenal.com/" + href.find("span", class_="field-content").find("a").get("href")
        hrefs.append(h)
    return hrefs



pars_href_list = pars_href()