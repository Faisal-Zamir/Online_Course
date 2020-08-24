from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . models import Profile, User, FollowUser

class UserAdmin(ModelAdmin):
    list_display = ["username", "first_name",'last_name','password','email']

admin.site.register(User,UserAdmin)


class FollowUserAdmin(ModelAdmin):
    list_display = ["profile", "followed_by"]

admin.site.register(FollowUser,FollowUserAdmin)


class ProfileAdmin(ModelAdmin):
    list_display = ["image", "phon"]

admin.site.register(Profile,ProfileAdmin)
