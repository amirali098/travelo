from django.urls import path

from . import views

from blog.feeds import LatestEntriesFeed

app_name='blog'

urlpatterns = [
    path("",views.home,name='home'),
    path("<int:id>",views.single_blog,name='blog-single'),
    path("category/<int:id>",views.home,name='category-filter'),
    path("tags/<str:tag_name>",views.home,name='tag'),
    path("Search",views.search,name='search'),
    path("rss/feed/", LatestEntriesFeed()),

]