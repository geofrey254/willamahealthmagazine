from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView,View, CreateView
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.conf import settings
from django.db.models import Q
from .models import Post, Category, Advert, Lists, News
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
    }    

    return render(request, 'home.html', context)

def registerPage(request):
    form    =      CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})

def CategoryView(request, slug):
    category      =   Category.objects.get(slug=slug)
    cats        =   Category.objects.all()
    adverts     =   Advert.objects.all()[0:1]
    latest      =   Post.objects.order_by('-created_on')[0:3]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]



    context =   {
        'category':category,
        'cats':cats,
        'adverts':adverts,
        'trending':trending,
        'latest':latest,

    }
    return render(request, "blog_category.html", context)

def article_detail(request, slug, *args, **kwargs):
    post        =   Post.objects.get(slug=slug)
    latest      =   Post.objects.order_by('-created_on')[0:4]
    adverts     =   Advert.objects.all()[0:1]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]

    context     =   {
        "post": post,
        'latest':latest, 
        'adverts':adverts,
        'trending':trending,
    }

    return render(request, "article.html", context)

# Posts delete and update panel
class CreatePost(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ('title','slug','author', 'blog_img','img_credits' ,'body' ,'blog_type', 'categories')
    

def post_update(request, slug):
    pass

def post_delete(request, slug):
    pass

# Latest Releases Views


def lists_page(request, *args, **kwargs):
    posts       =   Lists.objects.all()
    search_post =   request.GET.get('q')
    latest      =   Post.objects.order_by('-created_on')[0:4]
    adverts     =   Advert.objects.all()[0:1]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]



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
    }    

    return render(request, 'lists.html', context)

def list_detail(request, slug, *args, **kwargs):
    post        =   Lists.objects.get(slug=slug)
    latest      =   Post.objects.order_by('-created_on')[0:4]
    adverts     =   Advert.objects.all()[0:1]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]

    context     =   {
        "post": post,
        'latest':latest, 
        'adverts':adverts,
        'trending':trending,
    }

    return render(request, "list_detail.html", context)

def news(request, *args, **kwargs):
    posts       =   News.objects.all()
    search_post =   request.GET.get('q')
    latest      =   Post.objects.order_by('-created_on')[0:4]
    adverts     =   Advert.objects.all()[0:1]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]

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
    }    

    return render(request, 'news.html', context)

def news_detail(request, slug, *args, **kwargs):
    post        =   News.objects.get(slug=slug)
    latest      =   Post.objects.order_by('-created_on')[0:4]
    adverts     =   Advert.objects.all()[0:1]
    trending    =   Post.objects.filter(blog_type=2).order_by('-created_on')[0:3]

    context     =   {
        "post": post,
        'latest':latest, 
        'adverts':adverts,
        'trending':trending,
    }

    return render(request, "news_detail.html", context)