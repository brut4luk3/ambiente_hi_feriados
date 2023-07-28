from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(),
        label=_("E-mail"),
        error_messages={'required': 'Informe o seu e-mail.'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label=_("Senha"),
        strip=False,
        error_messages={'required': 'Informe a sua senha.'},
    )