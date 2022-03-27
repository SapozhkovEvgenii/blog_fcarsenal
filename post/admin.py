from statistics import mode
from django.contrib import admin
from post.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'created', 'image', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('post', 'author')


admin.site.register(Post, PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
