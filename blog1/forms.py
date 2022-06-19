from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    имя = forms.CharField(max_length=25)
    email = forms.EmailField()
    кому = forms.EmailField()
    комментарий = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    запрос = forms.CharField()
