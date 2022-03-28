from django.shortcuts import render
from home.utils.pars_fcarsenal import my_list_news
from home.models import News
from django.core.paginator import Paginator


def home_page(request):
    for elem in my_list_news:
        news = News()
        news.value = elem[0]
        news.href = elem[1]
        try:
            news.save()
        finally:
            continue
    all_news = News.objects.all()
    paginator = Paginator(all_news, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "news": all_news,
        "page_obj": page_obj
    }
    return render(request, "home.html", context)


def info_arsenal(request):
    return render(request, "about_arsenal.html")
