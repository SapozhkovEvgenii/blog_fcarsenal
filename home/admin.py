from django.contrib import admin
from home.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'href')
    search_fields = ('value',)


admin.site.register(News, NewsAdmin)