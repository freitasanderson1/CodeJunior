from django.urls import path
from .views import SubmissaoCreateView, ProblemasResolvidosListView
from cadastro.views import CustomUserCreateView, CustomLoginView

urlpatterns = [
    path('tentativa/', SubmissaoCreateView.as_view(), name='submeterTentativa'),
    path('resultado/', ProblemasResolvidosListView.as_view(), name='problemasResolvidos'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', CustomUserCreateView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),  # Use a classe de view

]
