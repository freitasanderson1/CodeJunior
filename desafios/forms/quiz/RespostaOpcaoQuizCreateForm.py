from django import forms

from desafios.models import RespostaQuiz

class RespostaOpcaoQuizCreateForm(forms.ModelForm):

    class Meta:
        model = RespostaQuiz
        exclude = ('dataCadastro', )