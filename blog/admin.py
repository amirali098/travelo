from django.contrib import admin
from .models import Post, Contact, Category,Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display='empty'
    list_display =('title','author','counted_views','status','published_date','login_requier',)
    list_filter = ('status','author')
    ordering = ['-created_date']
    search_fields = ['title','content']
    summernote_fields = ('content',)

admin.site.register(Post,PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    empty_value_display='empty'
    list_display =('name',)
    search_fields = ['name']

admin.site.register(Category,CategoryAdmin)


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')

admin.site.register(Contact,ContactAdmin)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'post', "approved",'created_date')
    list_filter = ('post','approved')
    search_fields = ('name', 'post')

admin.site.register(Comment,CommentAdmin)
