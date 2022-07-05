from django.urls import path
from api.views import PostAPIListView, PostAPIDetailView

urlpatterns = [
    path('posts/', PostAPIListView.as_view(), name='posts_list'),
    path('post/<pk>', PostAPIDetailView.as_view(),
         name='post_detail'),
]
