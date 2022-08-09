from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from Login.forms import LoginForm
from django.contrib.auth.models import User


class LoginView(View):
    def get(self, request):
        data = {'form': LoginForm()}
        return render(request, 'Login/login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            if username and password \
                    and authenticate(username=username, password=password):
                login(request, User)
                return HttpResponseRedirect(reverse('index'))

        data = {
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }
        return render(request, 'Login/login.html', data)
