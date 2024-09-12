from django.db import models

from desafios.models import Trilha, AlternativaOpcaoQuiz
from cadastro.models import Pessoa

class OpcaoQuiz(models.Model):
  titulo = models.TextField(u'Descrição da opção do quiz', max_length=200)
  alternativas = models.ManyToManyField(AlternativaOpcaoQuiz, verbose_name='Opções do Quiz', blank=False)

  ativo = models.BooleanField(verbose_name=u'Está ativo?',editable=True, default=True, help_text='Indica se a opcao está ativo')
  ordem = models.IntegerField(u'Ordenação', default=1,)

  class Meta:
    verbose_name = 'Opção do quiz'
    verbose_name_plural = 'Opções do quiz'

  def __str__(self):
      return f'{self.titulo}'
    
