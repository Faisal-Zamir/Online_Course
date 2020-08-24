from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic/')
    phon = models.IntegerField(blank=True, null=True, default="0")
    address = models.CharField(max_length=300, default="None")

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # def save(self):
    #     super().save()
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


class FollowUser(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile")
    followed_by = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="followed_by")
    def __str__(self):
        return "%s" % self.followed_by
