from django.shortcuts import render
from home.utils.pars_news import news_fcarsenal
from home.models import News
from django.views.generic import ListView


class ListNews(ListView):
    paginate_by = 10
    model = News
    template_name = "home.html"
    context_object_name = 'news'

    def get_queryset(self):
        for elem in news_fcarsenal:
            news = News()
            news.value = elem[0]
            news.href = elem[1]
            try:
                news.save()
            finally:
                continue
        all_news = News.objects.all()
        return all_news


def info_arsenal(request):
    context = {}
    if request.META.get("HTTP_REFERER"):
            context.update(back=request.META["HTTP_REFERER"])
    return render(request, "about_arsenal.html", context=context)
