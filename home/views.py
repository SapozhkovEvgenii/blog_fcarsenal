from django.shortcuts import render
# from home.utils.pars_fcarsenal import my_list_news
from home.models import News
from django.views.generic import ListView


class ListNews(ListView):
    paginate_by = 10
    model = News
    template_name = "home.html"
    context_object_name = 'news'

    # def get_news(self):
    #     for elem in my_list_news:
    #         news = News()
    #         news.value = elem[0]
    #         news.href = elem[1]
    #         try:
    #             news.save()
    #         finally:
    #             continue


def info_arsenal(request):
    return render(request, "about_arsenal.html")
