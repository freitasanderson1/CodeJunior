import subprocess
from django.views.generic.edit import CreateView
from problemasProgramacao.models.Submissao import Submissao

class SubmissaoCreateView(CreateView):
    model = Submissao
    fields = ['problema', 'codigo']
    template_name = 'submissaoForm.html'
    success_url = '/problemas/submeter-tentativa/'
    
    def form_valid(self, form):
        problema = form.cleaned_data['problema']
        codigo = form.cleaned_data['codigo']
        resultadoUsuario = self.executarCodigo(codigo)
    
        form.instance.usuario = self.request.user
        form.instance.resultado = resultadoUsuario
    
        if resultadoUsuario.strip() == problema.solucao.strip():
            form.instance.resultado = "Passou"
        else:
            form.instance.resultado = "Falhou"
        
        return super().form_valid(form)

    def executarCodigo(self, codigo):
        try:
            resultadoBytes = subprocess.check_output(['python', '-c', codigo], stderr=subprocess.STDOUT, timeout=10)
            resultadoStr = resultadoBytes.decode('utf-8')
            return resultadoStr
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')
        except subprocess.TimeoutExpired:
            return "Tempo limite excedido."
        
        