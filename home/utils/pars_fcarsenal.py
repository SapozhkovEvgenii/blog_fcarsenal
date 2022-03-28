from home.utils.class_parent import Parse
from home.utils.pars_href import pars_href_list


class NewsFCArsenal(Parse):

    def parser(self):
        list_news = []
        text_all = self.response().findAll("div", class_="views-field views-field-title")
        for elem in text_all:
            text_elem = elem.find("span", class_="field-content").find("a").text
            list_news.append(text_elem)
        return list_news

    def __iter__(self):
        self.cursor = 0
        self.lenght = len(self.parser())
        return self

    def __next__(self):
        if self.cursor < self.lenght:
            try:
                return self.parser()[self.cursor]
            finally:
                self.cursor += 1
        raise StopIteration


my_url = "https://fc-arsenal.com/news/all"

news_fcarsenal = NewsFCArsenal(my_url)

my_list_news = []

for i in zip(news_fcarsenal, pars_href_list):
    my_list_news.append(i)
