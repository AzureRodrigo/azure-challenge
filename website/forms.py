from django import forms


# Declaração dos campos do formulário de login
class FormLogin(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
