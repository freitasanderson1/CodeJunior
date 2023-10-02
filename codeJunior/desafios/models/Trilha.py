from django.db import models


class Trilha(models.Model):
    titulo = models.TextField(verbose_name="Titulo da trilha", max_length=300)
    descricao = models.TextField()
    desafios = models.ManyToManyField('Desafio', verbose_name="Desafios da trilha")  

    def __str__(self):
        return self.titulo
