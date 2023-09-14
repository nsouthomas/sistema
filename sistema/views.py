from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm

class Login(View):
    
    def get(self, request):
        form = LoginForm()
        return render(request, 'autenticacao.html', {'form': form, 'mensagem': ''})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('welcome')  # Redireciona para a página de boas-vindas após login
            else:
                form.add_error(None, "Usuário ou senha inválidos")
        return render(request, 'autenticacao.html', {'form': form})

def post_login_view(request):
    return HttpResponse("Bem-vindo!")
