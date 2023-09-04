from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')  # Personalize os campos conforme necessário
    username = forms.CharField(label= ('Nome de usuário'))
    password1 = forms.CharField(label= ('Senha'))
    password2 = forms.CharField(label= ('Confirmação de senha'))