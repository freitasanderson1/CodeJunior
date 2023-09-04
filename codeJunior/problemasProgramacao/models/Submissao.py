from django.db import models
from problemasProgramacao.models.Problema import Problema

class Submissao(models.Model):
    problema = models.ForeignKey(Problema, on_delete=models.CASCADE, related_name='submissao')
    codigo = models.TextField()
    resultado = models.CharField(max_length=100)  

    def __str__(self):
        return self.codigo
