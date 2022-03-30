from django.views.generic import ListView, DetailView, CreateView, FormView
from post.models import Post, Category
from post.forms import AddPostForm, AddCommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PostsView(ListView):
    paginate_by = 3
    model = Post
    template_name = "all_posts.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)
    

class ShowPost(DetailView, FormView):
    model = Post
    form_class = AddCommentForm
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all
        return context 

    def get_success_url(self):
        pk = self.kwargs['pk']
        success_url = f"/post/{pk}/"
        return success_url

    # @method_decorator(login_required)
    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author= self.request.user
        form.save()
        return super().form_valid(form) 


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

    def get_queryset(self):
        return Post.objects.filter(cat__id=self.kwargs['cat_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all
        context['cat'] = Category.objects.get(id=self.kwargs['cat_id'])
        return context 


# class AddComment(LoginRequiredMixin, CreateView):
#     form_class = AddCommentForm
#     template_name = 'addcomment.html'
#     success_url = reverse_lazy('posts')

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all
#         return context 


#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)