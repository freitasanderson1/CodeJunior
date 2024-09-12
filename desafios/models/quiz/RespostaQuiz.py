from django.db import models


from cadastro.models import Pessoa

class RespostaQuiz(models.Model):
  quemRespondeu = models.ForeignKey(Pessoa, verbose_name='Quem Respondeu', null=True, blank=True, default=None, on_delete=models.PROTECT)
  opcao = models.ForeignKey('OpcaoQuiz', verbose_name='Opção do Quiz', on_delete=models.PROTECT, null=False)
  alternativaSelecionada = models.ForeignKey('AlternativaOpcaoQuiz', verbose_name='Alternativa da opcao do Quiz', on_delete=models.PROTECT, null=False)
  quiz = models.ForeignKey('Quiz', verbose_name='Quiz', on_delete=models.PROTECT, null=False)
  
  dataCadastro = models.DateTimeField(u'Data de Cadastro', auto_now_add=True)

  class Meta:
    verbose_name = 'Resposta da opção do quiz'
    verbose_name_plural = 'Respostas da opções do quiz'

  def __str__(self):
      return f'{self.quiz} - {self.opcao}'
    
