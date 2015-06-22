from django import forms
from django.contrib.auth.models import User
from .models import Bookmark


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)

class EditForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('title', 'description', 'url',)

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('url',)