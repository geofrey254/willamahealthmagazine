from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('lists/', views.lists_page, name='lists'),
    path('news', views.news, name='news'),
    path('willama_health/<slug:slug>/', views.article_detail, name='article-detail'),
    path('willama_health/<slug:slug>/', views.list_detail, name='list-detail'),
    path('willama_health/news/<slug:slug>/', views.news_detail, name='news-detail'),
    path('willama_health/category/<slug:slug>/', views.CategoryView, name='blog_category'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)