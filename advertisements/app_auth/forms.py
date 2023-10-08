from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

user = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = user
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
        }

