from django.urls import path
from .views import SubmissaoCreateView

urlpatterns = [
    path('submeter-tentativa/', SubmissaoCreateView.as_view(), name='submeterTentativa'),
]
