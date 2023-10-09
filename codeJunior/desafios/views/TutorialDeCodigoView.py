from django.shortcuts import render, redirect
from .models import Codigo

class TutorialDeCodigoView(View):

    def get(self, request):
        codigos = Codigo.objects.all()
        return render(request, 'codigos.html', {'codigos': codigos})

    def post(self, request):
        titulo = request.POST['titulo']
        assunto = request.POST['assunto']
        trilha = request.POST['trilha']
        nivel = request.POST['nivel']
        quemCadastrou = request.user

        codigo = Codigo(titulo=titulo, assunto=assunto, trilha=trilha, nivel=nivel, quemCadastrou=quemCadastrou)
        codigo.save()

        return redirect('codigos')

    def put(self, request, codigo_id):
        codigo = Codigo.objects.get(id=codigo_id)

        titulo = request.POST['titulo']
        assunto = request.POST['assunto']
        trilha = request.POST['trilha']
        nivel = request.POST['nivel']

        codigo.titulo = titulo
        codigo.assunto = assunto
        codigo.trilha = trilha
        codigo.nivel = nivel
        codigo.save()

        return redirect('codigos')

    def delete(self, request, codigo_id):
        codigo = Codigo.objects.get(id=codigo_id)
        codigo.delete()

        return redirect('codigos')