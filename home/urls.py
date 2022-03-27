from django.urls import path
from home.views import info_arsenal, home_page

urlpatterns = [
    path("info", info_arsenal, name="info"),
    path("", home_page, name="home_page"),
]

