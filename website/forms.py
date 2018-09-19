from django import forms


# Declaração dos campos do formulário de login
class FormLogin(forms.Form):
    username = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
