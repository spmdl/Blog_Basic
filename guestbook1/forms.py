from django import forms
from .models import Comment
from django.forms import widgets
    
class CommentForm(forms.Form):
    name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'your name'}))
                           
    email = forms.EmailField(max_length=40, required=False, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'your email'}))
    text = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'name':'text','class': 'form-control','placeholder':'your doubt','style':'box-sizing:border-box','rows':'3'}))

    
