from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('lists/', views.lists_page, name='lists'),
    path('news', views.news, name='news'),
    path('willama_health/<slug:slug>/', views.article_detail, name='article-detail'),
    path('willama_health/<slug:slug>/', views.list_detail, name='list-detail'),
    path('willama_health/news/<slug:slug>/', views.news_detail, name='news-detail'),
    path('willama_health/category/<slug:slug>/', views.CategoryView, name='blog_category'),
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('admin_create/', views.CreatePost.as_view(), name='post-create'),
    path('post/slug/update/', views.post_update, name='post-update'),
    path('post/slug/delete/', views.post_delete, name='post-delete')
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)