from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Post,Comment


class PostAdmin(ModelAdmin):
    list_display = ["title", "content",'author','date_posted']
admin.site.register(Post, PostAdmin)

class CommentAdmin(ModelAdmin):
    list_display = ["name", "email",'body','created_on','post']
admin.site.register(Comment, CommentAdmin)
