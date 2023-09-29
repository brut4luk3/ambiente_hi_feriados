from django import forms
from django.utils.translation import gettext_lazy as _

class CustomAuthenticationForm(forms.Form):
    username = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control rounded-3'}),
        label=_("E-mail"),
        error_messages={'required': 'Informe o seu e-mail.'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control rounded-3'}),
        label=_("Senha"),
        strip=False,
        error_messages={'required': 'Informe a sua senha.'},
    )