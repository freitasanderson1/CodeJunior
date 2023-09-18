from django.db import models
from desafios.models import Desafio

from cadastro.models import Pessoa

class Submissao(models.Model):
    problema = models.ForeignKey(Desafio, on_delete=models.CASCADE, related_name='submissao')
    codigo = models.TextField()
    resultado = models.CharField(max_length=300)  
    pessoa = models.ForeignKey(Pessoa, verbose_name=u'Pessoa', null=False, on_delete=models.CASCADE)
    dataSubmissao = models.DateTimeField('Data de Submissão', auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.codigo}'
