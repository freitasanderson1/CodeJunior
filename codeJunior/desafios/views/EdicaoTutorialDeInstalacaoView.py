from django.shortcuts import render
from django.views.generic import TemplateView

class EdicaoTutorialDeInstalacaoView(TemplateView):
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
            'requisitos': [
                'Um computador com Windows, Mac ou Linux',
                'Uma conexão com a Internet',
            ],
            'instalacao': [
                'Acesse o site do Visual Studio Code',
                'Clique no botão "Download"',
                'Siga as instruções de instalação',
            ],
            'configuracao': [
                'Abra o Visual Studio Code',
                'Clique no botão "Extensions"',
                'Pesquise por "Python"',
                'Instale a extensão "Python"',
            ],
            'uso': [
                'Crie um novo arquivo Python',
                'Digite o código Python',
                'Salve o arquivo',
                'Execute o arquivo',
            ],
        }

        return render(request, self.template_name, dados)