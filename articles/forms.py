from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import Post

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model=User
        fields=('username','password','first_name','last_name','email',)


class AddPostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=('describe','link','title')