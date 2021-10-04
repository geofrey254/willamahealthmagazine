from django.contrib import admin
from .models import Post, Category, Advert, News

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','status','created_on', 'blog_type', 'status')
    list_filter=("status","blog_type","created_on","categories")
    search_fields=['title','body','blog_type']
    prepopulated_fields={'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
class NewsAdmin(admin.ModelAdmin):
    list_display=('title','slug','status','created_on', 'status')
    list_filter=("status","created_on")
    search_fields=['title','body']
    prepopulated_fields={'slug':('title',)}


admin.site.register(Post,PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Advert)
admin.site.register(News, NewsAdmin)

