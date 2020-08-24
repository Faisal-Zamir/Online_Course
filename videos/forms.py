from django import forms 
from .models import video

class VideoForm(forms.ModelForm):
    class Meta:
        model= video
        fields= ["title", "video"]