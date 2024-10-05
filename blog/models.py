from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse
from taggit.managers import TaggableManager


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image =models.ImageField(upload_to="blog/",default="blog/default.jpg")
    category=models.ManyToManyField(Category)
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    published_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    tags=TaggableManager()
    login_requier=models.BooleanField(default=False)


    class Meta:
        ordering=['-created_date']
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  reverse("blog:blog-single",kwargs={"id":self.id})

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=235)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    approved=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name