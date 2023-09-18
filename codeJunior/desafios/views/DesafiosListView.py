import subprocess
from django.views.generic.list import ListView
from desafios.models.Desafio import Desafio
from desafios.models.Submissao import Submissao
from desafios.forms import SubmissaoForm
from django.contrib.auth.mixins import LoginRequiredMixin

class DesafiosListView(LoginRequiredMixin, ListView):
    model = Desafio
    template_name = 'desafiosListView.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = []
        meses = [4, 5, 6, 7, 8, 9]
        submissoes = Submissao.objects.filter(problema__in=context["object_list"], pessoa__user=self.request.user)
        
        for mes in meses:
          _data = 0

          for submissao in submissoes:
              print(submissao.dataSubmissao.month, mes)
              if submissao.dataSubmissao.month == mes:
                  _data += 1
          data.append(_data)

          context['data'] = data
          context['submissoes'] = submissoes
          context['porcentagem'] = (100 * len(submissoes)) / len(context["object_list"])
        return context


    

        