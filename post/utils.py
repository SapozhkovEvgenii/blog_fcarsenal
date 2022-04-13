from post.models import Category


class DataMixin:
    def get_context(self, **kwargs):
        context = kwargs
        if self.request.META.get("HTTP_REFERER"):
            context.update(back=self.request.META["HTTP_REFERER"])
        context['categories'] = Category.objects.all
        return context
