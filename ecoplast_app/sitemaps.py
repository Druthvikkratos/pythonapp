# sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class MySitemap(Sitemap):
    def items(self):
        return ['index', 'about', 'contact','gallery','services'] 

    def location(self, item):
        return reverse(item)
