from django import forms
from django.core.validators import MinValueValidator

ENTRY_TYPE = (
    ("ENTRADA", 'Entrada'),
    ("SAIDA", 'Saida')
)

# Declaração dos campos do formulário de login
class FormLogin(forms.Form):
    username = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)


class FormInsert(forms.Form):
    type = forms.ChoiceField(
        label='Tipo de registro',
        required=True,
        choices=ENTRY_TYPE
    )
    name = forms.CharField(label='Nome do registro', required=True)
    value = forms.DecimalField(label='Valor em reais',
                               decimal_places=2,
                               max_digits=12,
                               validators=[MinValueValidator(0.01)]
                               )
