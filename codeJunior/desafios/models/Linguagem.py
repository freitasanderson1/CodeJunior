from django.db import models

class Linguagem(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(u'Nome', max_length=255)

    class Meta:
        verbose_name = 'Linguagem da Documentação'
        verbose_name_plural = 'Linguagem da Documentação'
        ordering = ['id','nome']

    def __str__(self):
        return f'{self.nome}'
