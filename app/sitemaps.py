from django.contrib.sitemaps import Sitemap
from app.models import *


class TestSitemap(Sitemap):
    changefreq = "weekly"  # always, hourly, daily, weekly, monthly, yearly
    priority = 0.8

    def items(self):
        return TestModel.objects.all()
