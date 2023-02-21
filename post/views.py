from django.views.generic import ListView, DetailView, CreateView, FormView
from post.models import Post, Category, Comment
from post.forms import AddPostForm, AddCommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from post.utils import DataMixin


class PostsView(DataMixin, ListView):
    paginate_by = 3
    model = Post
    template_name = "all_posts.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_context()
        return dict(list(context.items()) + list(context_mixin.items()))

    def get_queryset(self):
        return Post.objects.prefetch_related('cat').filter(is_published=True)


class ShowPost(DataMixin, DetailView, FormView):
    model = Post
    form_class = AddCommentForm
    template_name = 'post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            post_id=Post.objects.select_related('author').get(slug=self.kwargs['post_slug']).pk)
        context_mixin = self.get_context()
        return dict(list(context.items()) + list(context_mixin.items()))

    def get_success_url(self):
        url = self.kwargs['post_slug']
        success_url = f"/post/{url}/"
        return success_url

    def form_valid(self, form):
        post = Post.objects.get(slug=self.kwargs['post_slug'])
        form.instance.post = post
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class AddPost(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'addpost.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCategory(DataMixin, ListView):
    paginate_by = 3
    model = Post
    template_name = 'category_index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.select_related('author').filter(cat__id=self.kwargs['cat_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_context(
            cat=Category.objects.get(id=self.kwargs['cat_id']))
        return dict(list(context.items()) + list(context_mixin.items()))
