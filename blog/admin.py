from django.contrib import admin

from .models import BlogPost, Category, ViewPost, Like, Comment

admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(ViewPost)
admin.site.register(Like)
admin.site.register(Comment)
