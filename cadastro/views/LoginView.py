from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy

class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'cadastro/login.html'
    
    def form_valid(self, form):
        print('Válido')
        super().form_valid(form)
        messages.success(self.request, "Login bem-sucedido.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Credenciais inválidas. Verifique seu CPF e senha.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('desafios-list')  