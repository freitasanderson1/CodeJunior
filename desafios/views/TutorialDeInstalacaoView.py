from django.shortcuts import render
from django.views.generic import TemplateView

class TutorialDeInstalacaoView(TemplateView):
    template_name = 'documentacao.html'

    def get(self, request, *args, **kwargs):
        dados = {
            'titulo': 'Documentação do Visual Studio Code',
            'assunto': 'Como baixar, configurar e usar o Visual Studio Code',
            'trilha': 'Python',
            'quemCadastrou': 'Usuario',
            'dataCadastro': datetime.datetime.now(),
            'dataAlteracao': datetime.datetime.now(),
            'ativo': True,
        }

        return render(request, self.template_name, dados)