from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post, Lists, News
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'lists', 'news']

    def location(self, item):
        return reverse(item)

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()

class ListsSitemap(Sitemap):
    def items(self):
        return Lists.objects.all()

class NewsSitemap(Sitemap):
    def items(self):
        return News.objects.all()