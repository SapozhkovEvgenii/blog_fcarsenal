from django.urls import path
from home.views import info_arsenal, listnews

urlpatterns = [
    path("info", info_arsenal, name="info"),
    path("", listnews, name="home_page"),
]

