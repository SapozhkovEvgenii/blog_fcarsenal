# Generated by Django 4.0.1 on 2022-05-31 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, null=True, verbose_name='URL'),
        ),
    ]
