from django.urls import path
from .views import SubmissaoCreateView, DesafiosResolvidosListView, DesafiosListView
from cadastro.views import LoginView, SairView, CadastroView

urlpatterns = [
    path('', DesafiosListView.as_view(), name="desafios-list"),
    path('tentativa/', SubmissaoCreateView.as_view(), name='submeterTentativa'),
    path('resultado/', DesafiosResolvidosListView.as_view(), name='desafioResolvido'),

    #Logins views
    path('login/', LoginView.as_view(), name='login'),
    path('sair/', SairView.as_view(), name='sair'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
]
