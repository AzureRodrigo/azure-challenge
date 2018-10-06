import requests
import json
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login

from rest_framework.authtoken.models import Token

from website.forms import FormLogin, FormInsert


# View responsável pelo login
class ViewLoginMail(TemplateView):
    # override de criação e carregamento da tela
    def get(self, *args, **kwargs):
        form = FormLogin()
        return render(self.request, 'website/login.html', {'form': form})

    # override do envio de informações do formulário
    def post(self, *args, **kwargs):
        form = FormLogin(self.request.POST)

        if form.is_valid():
            user = authenticate(email=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(self.request, user)
                    token = Token.objects.get(user=user)
                    if token is None:
                        token = Token.objects.create(user=user)
                    self.request.session['token'] = token.key
                    return redirect('/index')
            else:
                return render(self.request, 'website/login.html', {'error_message': 'Credenciais inválidas!',
                                                                   'form': form})

        return render(self.request, 'website/login.html')


# View responsável pela consulta e adição de registors
# Ultiza as chamadas criadas na api para consulta e inserção
def view_login_index(request):
    # verifica se o usuário está logado caso não esteja manda para o login
    if 'token' not in request.session:
        return redirect('login')

    _url = "http://127.0.0.1:8000/"
    _token = request.session['token']
    _headers = {
        "Content-Type": "application/json",
        "Authorization": "Token " + _token
    }

    # Formulário de adição de resistros
    if request.method == "POST":
        form = FormInsert(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            _data = {
                "tipo_de_registro": info['type'],
                "nome_do_registro": info['name'],
                "valor_em_reais": str(info['value'])
            }
            requests.post(_url + 'api/post_registers/',
                          headers=_headers,
                          data=json.dumps(_data))
            return redirect('/index')

    else:
        form = FormInsert()

    # chamada dos registros do servidor
    _result = requests.get(
        _url + 'api/get_registers/',
        headers=_headers
    )
    data = _result.json()

    kwargs = {'object_list': data, 'form': form}
    return render(request, 'website/index.html', kwargs)
