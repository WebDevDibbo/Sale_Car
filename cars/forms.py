from django import forms
from .models import PostCar, Comment

class CarPostForm(forms.ModelForm):
    class Meta:
        model = PostCar
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']