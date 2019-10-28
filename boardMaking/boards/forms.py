from django import forms
from .models import Board, Comment, ReComment


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = {'title', 'content'}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'userName', 'content'}


class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = {'userName', 'content'}
