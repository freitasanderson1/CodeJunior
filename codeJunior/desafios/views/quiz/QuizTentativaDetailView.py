from django.views.generic import DetailView
#
from desafios.models import Quiz, RespostaQuiz, OpcaoQuiz

class QuizTentativaDetailView(DetailView):
  model = Quiz
  template_name = 'quiz/quizTentativaDetailView.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      quiz = self.get_object()
      opcoesRespondidas = RespostaQuiz.objects.filter(quiz=quiz)
      context["opcoesRespondidas"] = opcoesRespondidas
      context["respostasCorretas"] = opcoesRespondidas.filter(alternativaSelecionada__correta=True)
      context["respostasIncorretas"] = opcoesRespondidas.filter(alternativaSelecionada__correta=False)
      context["opcao"] = OpcaoQuiz.objects.filter(quiz=quiz).exclude(pk__in=opcoesRespondidas.values_list('opcao__pk')).first()
      return context


        