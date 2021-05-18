from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('the_savanna_wave_lists/', views.lists_page, name='lists'),
    path('the_savanna_wave/news', views.news, name='news'),
    path('the_savanna_wave_latest_releases/', views.releases, name='releases'),
    path('the_savanna_wave/<slug:slug>/', views.article_detail, name='article-detail'),
    path('the_savanna_wave_lists/<slug:slug>/', views.list_detail, name='list-detail'),
    path('the_savanna_wave/news/<slug:slug>/', views.news_detail, name='news-detail'),
    path('the_savanna_wave/category/<slug:slug>/', views.CategoryView, name='blog_category'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)