from django.db import models
# from django.conf import settings
from users.models import User
class video(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=300,)
    video= models.FileField(upload_to='videos/', null=True)



