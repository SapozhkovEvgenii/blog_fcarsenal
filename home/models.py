from django.db import models


class News(models.Model):
    value = models.TextField(unique=True, verbose_name="Title news")
    href = models.TextField(unique=True)


    class Meta:
        db_table = "news"
        verbose_name = "New"

    def __str__(self):
        return self.value
        
