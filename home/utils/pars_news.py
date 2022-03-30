import requests
from bs4 import BeautifulSoup as BS

my_url = "https://www.justarsenal.com/category/arsenal-news"


def parser():
    response = requests.get(my_url)
    page = BS(response.text, 'lxml')
    text_all = page.findAll("div", class_="img-txt")
    list_news = []
    href_news = []
    my_list_news = []
    for elem in text_all:
        text_elem = elem.find("a").text
        href_elem = elem.find("a").get("href")
        list_news.append(text_elem)
        href_news.append(href_elem)
    for i in zip(list_news, href_news):
        my_list_news.append(i)
    return my_list_news

news_fcarsenal = parser()


