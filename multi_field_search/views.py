# search.views.py
from itertools import chain
from django.views.generic import ListView

from .models import Post
from .models import Lesson
from .models import Profile


class SearchView(ListView):
    template_name = 'search.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            blog_results = Post.objects.search(query)
            lesson_results = Lesson.objects.search(query)
            profile_results = Profile.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                blog_results,
                lesson_results,
                profile_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Post.objects.none()  # just an empty queryset as default


search = SearchView.as_view()
