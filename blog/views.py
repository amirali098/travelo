from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Post, Comment
from django.utils import timezone
from blog.forms import CommentForm, NewsletterForm
from django.contrib import messages


# Create your views here.

def home(request, id=None, tag_name=None):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if id:
        posts = posts.filter(category__id=id)
    if tag_name:
        posts = posts.filter(tags__name=tag_name)

        print(tag_name)
        print(posts)

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"posts":  page_obj}
    return render(request, 'Blog/blog.html', context)


def single_blog(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Submit Succsesfully")
        else:
            messages.add_message(request, messages.ERROR, "Not Succsesfully")

    post = get_object_or_404(Post, pk=id, status=1, published_date__lte=timezone.now())
    if post.login_requier == False:
        next_post = Post.objects.filter(id__gt=post.id, status=1, published_date__lte=timezone.now()).order_by('id').first()
        previous_post = Post.objects.filter(id__lt=post.id, status=1, published_date__lte=timezone.now()).order_by('id').first()
        post.counted_views += 1
        post.save()
        comments = Comment.objects.filter(post=post.id, approved=True).order_by("-created_date")
        form = CommentForm()
        context = {'post': post,
                   "next_post": next_post,
                   "previous_post": previous_post,
                   "comments": comments,
                   "form": form}
        return render(request, 'Blog/single-blog.html', context)
    elif request.user.is_authenticated:
        next_post = Post.objects.filter(id__gt=post.id, status=1, published_date__lte=timezone.now()).order_by('id').first()
        previous_post = Post.objects.filter(id__lt=post.id, status=1, published_date__lte=timezone.now()).order_by('id').first()
        post.counted_views += 1
        post.save()
        comments = Comment.objects.filter(post=post.id, approved=True).order_by("-created_date")
        form = CommentForm()
        context = {'post': post,
                   "next_post": next_post,
                   "previous_post": previous_post,
                   "comments": comments,
                   "form": form}
        return render(request, 'Blog/single-blog.html', context)
    else:
        return redirect("accounts:login")


def search(request):
    posts = Post.objects.filter(status=1)
    if request.method == "GET":
        if s := request.GET.get("s"):
            posts = posts.filter(content__contains=s)
    context = {"posts": posts}
    return render(request, 'Blog/blog.html', context)




def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed to the newsletter!')
            return redirect('Main:home')
        else:
            messages.add_message(request, messages.ERROR, "Not Succsesfully")
            return redirect('Main:home')

    else:
        form = NewsletterForm()
        return render(request, 'Blog/blog.html')
