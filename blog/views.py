from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView,View, CreateView
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.db.models import Q
from .models import Post, Category, Advert, Lat_Real, Lists, News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

# Create your views here.
def home(request, *args, **kwargs):
    posts       =   Post.objects.all()
    search_post =   request.GET.get('q')
    cats        =   Category.objects.all()
    latest      =   Post.objects.order_by('-created_on')[0:3]
    featured    =   Post.objects.filter(blog_type=1).order_by('-created_on')[0:2]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]
    adverts     =   Advert.objects.all()[0:1]
    trend_music     =   Lat_Real.objects.filter(music_type=1).order_by('-created_on')


# Search filter
    if search_post:
        posts   =   Post.objects.filter(Q(title__icontains=search_post)|Q(body__icontains=search_post)).distinct()
        featured   =   Post.objects.filter(Q(title__icontains=search_post)|Q(body__icontains=search_post)).distinct()
    else:
        posts   =   Post.objects.filter(status=1).order_by('-created_on')
        featured   =   Post.objects.filter(blog_type=1).order_by('-created_on')[0:2]
        
    paginator   = Paginator(posts, 3)
    page        =   request.GET.get('page')
    try:
        posts   =   paginator.page(page)
    except PageNotAnInteger:
        posts   =   paginator.page(1)
    except EmptyPage:
        posts   =   paginator.page(paginator.num_pages)


    context     =   {
        'posts':posts,
        'latest':latest,
        'cats':cats,
        'featured':featured,
        'trending':trending,
        'adverts':adverts,
        'trend_music':trend_music
    }    

    return render(request, 'home.html', context)

# contact page views start here
def contact(request):
    if request.method == 'POST':
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('contact_content')

            send_mail(
                contact_name,
                contact_content,
                contact_email,
                ['devongeoffreymaina@gmail.com'],
                )
           
            return render (request, 'contact.html',{'contact_name': contact_name})
    
    else:
            return render (request, 'contact.html')

def CategoryView(request, slug):
    category      =   Category.objects.get(slug=slug)
    cats        =   Category.objects.all()
    adverts     =   Advert.objects.all()[0:1]
    latest      =   Post.objects.order_by('-created_on')[0:3]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]
    trend_music     =   Lat_Real.objects.filter(music_type=1).order_by('-created_on')



    context =   {
        'category':category,
        'cats':cats,
        'adverts':adverts,
        'trending':trending,
        'latest':latest,
        'trend_music':trend_music

    }
    return render(request, "blog_category.html", context)

def article_detail(request, slug, *args, **kwargs):
    post        =   Post.objects.get(slug=slug)
    latest      =   Post.objects.order_by('-created_on')[0:4]
    adverts     =   Advert.objects.all()[0:1]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]
    trend_music     =   Lat_Real.objects.filter(music_type=1).order_by('-created_on')

    context     =   {
        "post": post,
        'latest':latest, 
        'adverts':adverts,
        'trending':trending,
        'trend_music':trend_music
    }

    return render(request, "article.html", context)

# Latest Releases Views
def releases(request, *args, **kwargs):
    release     =   Lat_Real.objects.order_by('-created_on')
    trend_music     =   Lat_Real.objects.filter(music_type=1).order_by('-created_on')

    context     =   {
        'release':release,
        'trend_music':trend_music    
    }

    return render(request, "releases.html", context)

def lists_page(request, *args, **kwargs):
    posts       =   Lists.objects.all()
    search_post =   request.GET.get('q')
    latest      =   Post.objects.order_by('-created_on')[0:4]
    adverts     =   Advert.objects.all()[0:1]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]
    trend_music     =   Lat_Real.objects.filter(music_type=1).order_by('-created_on')



# Search filter
    if search_post:
        posts       =   Lists.objects.filter(Q(title__icontains=search_post)|Q(body__icontains=search_post)).distinct()
    else:
        posts   =   Lists.objects.filter(status=1).order_by('-created_on')
        
    paginator   = Paginator(posts, 3)
    page        =   request.GET.get('page')
    try:
        posts   =   paginator.page(page)
    except PageNotAnInteger:
        posts   =   paginator.page(1)
    except EmptyPage:
        posts   =   paginator.page(paginator.num_pages)


    context     =   {
        'posts':posts,
        'latest':latest, 
        'adverts':adverts,
        'trending':trending,
        'trend_music':trend_music
    }    

    return render(request, 'lists.html', context)

def list_detail(request, slug, *args, **kwargs):
    post        =   Lists.objects.get(slug=slug)
    latest      =   Post.objects.order_by('-created_on')[0:4]
    adverts     =   Advert.objects.all()[0:1]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]
    trend_music     =   Lat_Real.objects.filter(music_type=1).order_by('-created_on')

    context     =   {
        "post": post,
        'latest':latest, 
        'adverts':adverts,
        'trending':trending,
        'trend_music':trend_music
    }

    return render(request, "list_detail.html", context)

def news(request, *args, **kwargs):
    posts       =   News.objects.all()
    search_post =   request.GET.get('q')
    latest      =   Post.objects.order_by('-created_on')[0:4]
    adverts     =   Advert.objects.all()[0:1]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]
    trend_music     =   Lat_Real.objects.filter(music_type=1).order_by('-created_on')

# Search filter
    if search_post:
        posts       =   News.objects.filter(Q(title__icontains=search_post)|Q(body__icontains=search_post)).distinct()
    else:
        posts   =   News.objects.filter(status=1).order_by('-created_on')
        
    paginator   = Paginator(posts, 3)
    page        =   request.GET.get('page')
    try:
        posts   =   paginator.page(page)
    except PageNotAnInteger:
        posts   =   paginator.page(1)
    except EmptyPage:
        posts   =   paginator.page(paginator.num_pages)


    context     =   {
        'posts':posts,
        'latest':latest, 
        'adverts':adverts,
        'trending':trending,
        'trend_music':trend_music
    }    

    return render(request, 'news.html', context)

def news_detail(request, slug, *args, **kwargs):
    post        =   News.objects.get(slug=slug)
    latest      =   Post.objects.order_by('-created_on')[0:4]
    adverts     =   Advert.objects.all()[0:1]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]
    trend_music     =   Lat_Real.objects.filter(music_type=1).order_by('-created_on')

    context     =   {
        "post": post,
        'latest':latest, 
        'adverts':adverts,
        'trending':trending,
        'trend_music':trend_music
    }

    return render(request, "news_detail.html", context)