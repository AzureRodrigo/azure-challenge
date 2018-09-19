from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login

from website.forms import FormLogin


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
                    return redirect('/api')
                    # return HttpResponseRedirect(reverse('api'))
            else:
                return render(self.request, 'website/login.html', {'error_message': 'Credenciais inválidas!',
                                                                   'form': form})

        return render(self.request, 'website/login.html')
