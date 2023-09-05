from django.db import models

CHOICE_DIFICULDADES = (
    (1, 'Básico'),
    (2, 'Intermediário'),
    (3, 'Avançado'),
)

class Desafio(models.Model):

    titulo = models.CharField(u'Título do Desafio',max_length=200)
    descricao = models.TextField(u'Descrição do Desafio')
    solucao = models.CharField(u'Solução do Desafio', help_text='Solução do desafio ou saída esperada', max_length=200)
    dificuldade = models.CharField(u'Nível do Desafio', choices=CHOICE_DIFICULDADES)

    def __str__(self):
        return f'{self.id} - {self.titulo}'
