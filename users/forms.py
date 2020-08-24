from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model  = User
        #fields = '__all__'
        fields = ['username', 'email','password1','password2',]