from django.conf import settings
from django.urls import URLPattern, URLResolver

urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])


def list_urls(lis, acc=None):
    if acc is None:
        acc = []
    if not lis:
        return
    li = lis[0]
    if isinstance(li, URLPattern):
        yield acc + [str(li.pattern)]
    elif isinstance(li, URLResolver):
        yield from list_urls(li.url_patterns, acc + [str(li.pattern)])
    yield from list_urls(lis[1:], acc)


def url_list():
    urls = list()
    for p in list_urls(urlconf.urlpatterns):
        urls.append(''.join(p))
    return urls
