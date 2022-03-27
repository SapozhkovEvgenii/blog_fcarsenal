from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from post.models import Post, Category
from post.forms import AddPostForm, AddCommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PostsView(ListView):
    paginate_by = 3
    model = Post
    template_name = "all_posts.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all
        # context['cat_select'] = 0
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)
    

class ShowPost(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all
        return context 



class AddPost(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'addpost.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCategory(ListView):
    paginate_by = 3
    model = Post
    template_name = 'category_index.html'
    context_object_name = 'posts'
    # allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(cat__id=self.kwargs['cat_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all
        context['cat'] = Category.objects.get(id=self.kwargs['cat_id'])
        return context 


class AddComment(LoginRequiredMixin, CreateView):
    form_class = AddCommentForm
    template_name = 'addcomment.html'
    success_url = reverse_lazy('posts')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all
        # context['post'] = Post
        return context 

    def form_valid(self, form):
        form.instance.author = self.request.user
        # form.instance.post_id = self.request.post.pk
        return super().form_valid(form)