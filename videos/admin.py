from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import video

class videoAdmin(ModelAdmin):
    list_display = ["title", "video",'user_id']

admin.site.register(video, videoAdmin)