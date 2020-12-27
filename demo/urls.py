from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from app.sitemaps import TestSitemap

sitemaps = {
    "test_sitemap": TestSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'), name='allauth'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
    path('', include('pwa.urls')),
    path('', include('app.urls')),
    path('', include('imagecrop.urls')),
    path('', include('multi_field_search.urls')),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
