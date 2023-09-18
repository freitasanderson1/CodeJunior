import subprocess
from django.views.generic import DetailView
from desafios.models.Desafio import Desafio
from desafios.models.Submissao import Submissao
from desafios.forms import SubmissaoForm

class DesafiosDetailView(DetailView):
    model = Desafio
    template_name = 'desafiosDetailView.html'



    

        