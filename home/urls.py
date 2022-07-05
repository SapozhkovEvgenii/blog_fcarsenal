from django.urls import path
from home.views import info_arsenal, ListNews

urlpatterns = [
    path("info", info_arsenal, name="info"),
    path("", ListNews.as_view(), name="home_page"),
]
