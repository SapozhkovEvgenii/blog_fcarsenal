from django.db import models
from user.models import User
from datetime import datetime
from random import randint
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.conf import settings
from django.urls import reverse


class Post(models.Model):

    def file_path(self, filename):
        file_expansion = filename.split(".")[-1]
        file_name = filename.split(".")[0]
        path_file = datetime.strftime(datetime.now(), "photos/%Y/%m/%d/")
        return path_file + file_name + str(randint(10000000, 99999999)) + \
            "." + file_expansion

    title = models.CharField(
        max_length=256, unique=True, verbose_name="Post title")
    cat = models.ManyToManyField("Category", related_name="posts")
    author = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.CASCADE,
        verbose_name="Post author"
    )
    content = models.TextField(verbose_name="Post content")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Time created")
    updated = models.DateField(auto_now=True, verbose_name="Time updated")
    image = models.ImageField(upload_to=file_path)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")

    def __str__(self):
        return (self.title[:25] + "...") if len(self.title) > 25 else self.title

    def get_absolute_url(self):
        return reverse('post_user', kwargs={'post_slug': self.slug})

    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        ordering = ["-created"]


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.id})

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["id"]


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField(verbose_name="Comment content")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Time created")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.author}" + \
            " " + datetime.strftime(self.created, "%Y/%m/%d %H:%M:%S ")

    class Meta:
        db_table = "comments"
        verbose_name = "Comment"
        ordering = ["-created"]


@receiver(pre_delete, sender=Post)
def delete_image(sender, instance, **kwargs):
    path_to_file = settings.MEDIA_ROOT/str(instance.image.path)
    path_to_file.unlink()
