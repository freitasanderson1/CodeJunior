import subprocess
from django.views.generic.list import ListView
from problemasProgramacao.models.Problema import Problema
from problemasProgramacao.models.Submissao import Submissao
from problemasProgramacao.forms import SubmissaoForm

class ProblemasResolvidosListView(ListView):
    model = Problema
    template_name = 'problemasResolvidos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code = Submissao.objects.all().last()
        resultadoBytes = subprocess.check_output(['python', '-c', code.codigo], stderr=subprocess.STDOUT, timeout=10)
        resultadoStr = resultadoBytes.decode('utf-8')
        context["codigo"] = resultadoStr
        return context
    

        