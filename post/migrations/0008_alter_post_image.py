# Generated by Django 4.0.1 on 2022-03-23 11:36

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=post.models.Post.file_path),
        ),
    ]
