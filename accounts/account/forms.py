from django import forms
from django.contrib.auth import get_user_model


class UserForm(forms.ModelForm):
    class Metal:
        model = get_user_model()
        fields = ['username', 'password']
