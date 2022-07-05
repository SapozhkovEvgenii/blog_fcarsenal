from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'cat', 'author', 'content',
                  'created', 'updated', 'slug')
