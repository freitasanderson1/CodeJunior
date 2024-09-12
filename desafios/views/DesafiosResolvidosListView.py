import subprocess
from django.views.generic.list import ListView
from desafios.models.Desafio import Desafio
from desafios.models.Submissao import Submissao
from desafios.forms import SubmissaoForm

class DesafiosResolvidosListView(ListView):
    model = Desafio
    template_name = 'desafioResolvido.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code = Submissao.objects.all().last()
        resultadoBytes = subprocess.check_output(['python', '-c', code.codigo], stderr=subprocess.STDOUT, timeout=10)
        resultadoStr = resultadoBytes.decode('utf-8')
        context["codigo"] = resultadoStr
        return context
    

        