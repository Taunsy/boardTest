from django import forms
from .models import Board, Comment, ReComment


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = {'title', 'content', 'username'}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'username', 'content'}


class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = {'username', 'content'}
