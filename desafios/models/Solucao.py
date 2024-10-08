from django.db import models

from desafios.models import Desafio

class Solucao(models.Model):
  desafio = models.ForeignKey(Desafio, verbose_name='Desafio', on_delete=models.PROTECT, null=False)

  entrada = models.CharField(u'Solucao', max_length=200)
  secreta = models.BooleanField(verbose_name=u'Secreta?',editable=True, default=True, help_text='Indica se o solucao é secreta')

  ativo = models.BooleanField(verbose_name=u'Está ativo?',editable=True, default=True, help_text='Indica se o solucao está ativo')

  class Meta:
    verbose_name = 'Solução do desafio'
    verbose_name_plural = 'Soluções dos desafios'

  def __str__(self):
      return f'Solução {self.id} - {self.desafio}'
    
