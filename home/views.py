from django.shortcuts import render
from home.utils.pars_news import news_fcarsenal
from home.models import News
from django.views.generic import ListView
from django.core.paginator import Paginator


def listnews(request):
    for elem in news_fcarsenal:
        news = News()
        news.value = elem[0]
        news.href = elem[1]
        try:
            news.save()
        finally:
            continue
    all_news = News.objects.all()
    paginator = Paginator(all_news, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "news": all_news,
        "page_obj": page_obj
    }
    return render(request, "home.html", context)


def info_arsenal(request):
    return render(request, "about_arsenal.html")

