from django.urls import path
from post.views import PostCategory, PostsView, ShowPost, AddPost, PostCategory
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("posts/", cache_page(60)(PostsView.as_view()), name="posts"),
    path("post/<int:pk>/", ShowPost.as_view(), name="post_user"),
    path("addpost/", AddPost.as_view(), name="add_post"),
    path("categories/<int:cat_id>/", cache_page(60)(PostCategory.as_view()), name="category"),
    # path("addcomment/", AddComment.as_view(), name="add_comment")
]

