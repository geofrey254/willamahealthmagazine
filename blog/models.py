import sys
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from tinymce import models as tinymce_models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.template.defaultfilters import slugify

STATUS=(
    (0,"Draft"),
    (1,"Publish")
)

TYPE=(
    (0,"None"),
    (1,"Featured"),
    (2,"Trending")
)

LABEL=(
    (0, "None"),
    (1, "Trending")
)

class Category(models.Model):
    title   =   models.CharField(max_length=20, unique=True, null=True)
    slug        =   models.SlugField(max_length=250, unique=True,null=True)

    class Meta:
        verbose_name_plural =   'categories'

    def get_absolute_url(self):
        return reverse('blog_category', args=[self.slug])


    def __str__(self):
        return self.title

class Post(models.Model):
    title       =   models.CharField(max_length=255, unique=True)
    blog_img    =   models.ImageField(upload_to="blog_pics/", null=True, blank=True)
    img_credits =   models.CharField(max_length=255, null=True)
    slug        =   models.SlugField(max_length=250, null=True, blank=True, unique=True)
    author      =   models.CharField(max_length=100, default='Menim')
    updated_on  =   models.DateTimeField(auto_now=True)
    body        =   tinymce_models.HTMLField()
    created_on  =   models.DateTimeField(auto_now_add=True)
    status      =   models.IntegerField(choices=STATUS, default=0)
    blog_type   =   models.IntegerField(choices=TYPE, default=0)
    categories  =   models.ManyToManyField(Category, related_name='posts')


    class Meta:
        ordering    =   ['-created_on']

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.blog_img   =   self.compressImage(self.blog_img)
        super(Post, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def compressImage(self,blog_img):
        imageTemporary  =   Image.open(blog_img)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        blog_img    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % blog_img.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return blog_img

class Advert(models.Model):
    adv = models.ImageField(upload_to="ads/", null=True, blank=True)
    title       =   models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.adv   =   self.compressImage(self.adv)
        super(Advert, self).save(*args, **kwargs)

        
    
    def compressImage(self,adv):
        imageTemporary  =   Image.open(adv)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        adv    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % adv.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return adv
class Lists(models.Model):
    title       =   models.CharField(max_length=255, unique=True)
    blog_img    =   models.ImageField(upload_to="blog_pics/", null=True, blank=True)
    img_credits =   models.CharField(max_length=255, null=True)
    slug        =   models.SlugField(max_length=250, null=True, blank=True, unique=True)
    author      =   models.CharField(max_length=100, default='Menim')
    updated_on  =   models.DateTimeField(auto_now=True)
    body        =   tinymce_models.HTMLField()
    created_on  =   models.DateTimeField(auto_now_add=True)
    status      =   models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering    =   ['-created_on']
        verbose_name_plural =   'Lists'

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('list-detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.blog_img   =   self.compressImage(self.blog_img)
        super(Lists, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def compressImage(self,blog_img):
        imageTemporary  =   Image.open(blog_img)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        blog_img    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % blog_img.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return blog_img

class News(models.Model):
    title       =   models.CharField(max_length=255, unique=True)
    blog_img    =   models.ImageField(upload_to="blog_pics/", null=True, blank=True)
    img_credits =   models.CharField(max_length=255, null=True)
    slug        =   models.SlugField(max_length=250, null=True, blank=True, unique=True)
    author      =   models.CharField(max_length=100, default='Menim')
    updated_on  =   models.DateTimeField(auto_now=True)
    body        =   tinymce_models.HTMLField()
    created_on  =   models.DateTimeField(auto_now_add=True)
    status      =   models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering    =   ['-created_on']
        verbose_name_plural =   'News'

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('news-detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.blog_img   =   self.compressImage(self.blog_img)
        super(News, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def compressImage(self,blog_img):
        imageTemporary  =   Image.open(blog_img)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        blog_img    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % blog_img.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return blog_img