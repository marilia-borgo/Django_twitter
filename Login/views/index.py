from audioop import reverse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, View):
    
    def get(self, request):
        data = { 'user': request.user }
        return redirect('post/logado')