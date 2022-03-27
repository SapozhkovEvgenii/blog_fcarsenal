from django.urls import path
from post.views import PostCategory, PostsView, ShowPost, AddPost, PostCategory, AddComment

urlpatterns = [
    path("posts/", PostsView.as_view(), name="posts"),
    path("post/<int:pk>/", ShowPost.as_view(), name="post_user"),
    path("addpost/", AddPost.as_view(), name="add_post"),
    path("categories/<int:cat_id>/", PostCategory.as_view(), name="category"),
    path("addcomment/", AddComment.as_view(), name="add_comment")
]

