from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from cadastro.forms.CadastroForm import CadastroForm
from cadastro.models.Pessoa import Pessoa

class CadastroView(CreateView):
    template_name = 'cadastro/cadastro.html'
    form_class = CadastroForm
    model = User
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['form'] = self.form_class

        return context

    def dispatch(self, request, *args, **kwargs):
        print('Caiu dispatch')
        usuario = request.user

        if request.POST:
            try:
                check_existe_usuario = User.objects.get(username=request.POST['cpf'])
            except:
                check_existe_usuario = None

            if check_existe_usuario:
                messages.error(self.request, "Ocorreu um erro ao realizar seu cadastro, um usuário com este CPF já existe!")
                return redirect('cadastro')

            print(request.POST)

            novo_usuario = User()

            novo_usuario.first_name = request.POST.get('nome')
            novo_usuario.last_name = request.POST.get('sobrenome')
            novo_usuario.username = request.POST.get('cpf')
            novo_usuario.email = request.POST.get('email')
            senha = request.POST.get('senha')
            senhaConfirma = request.POST.get('senhaConfirma')

            print(novo_usuario)
            
            if senha != senhaConfirma:
                print('Senha não é igual')
                messages.error(self.request, "Ocorreu um erro ao realizar seu cadastro, as senhas não são iguais!")
                return redirect('cadastro')

            else:
                senha_criptografada = make_password(password=request.POST['senha'], salt=None, hasher='pbkdf2_sha256')
                corresponde = check_password(password=senha, encoded=senha_criptografada)

                if corresponde:
                    novo_usuario.password = senha_criptografada
                    print('Passou!')
                    
                    novo_usuario.save()

                    nova_pessoa = Pessoa()
                    nova_pessoa.user = novo_usuario
                    nova_pessoa.nomeCompleto = f'{novo_usuario.get_full_name()}'
                    nova_pessoa.cpf = novo_usuario.username
                    nova_pessoa.email = novo_usuario.email
                    nova_pessoa.contato = request.POST["telefone"]
                    nova_pessoa.sexo = request.POST['sexo']
                    nova_pessoa.dataNascimento = request.POST['dataNascimento']
                    nova_pessoa.save()

                    messages.success(self.request, "Cadastro bem-sucedido.")
                else:
                    messages.error(self.request, "Ocorreu um erro ao realizar seu cadastro. Tente novamente!")
                    
        if usuario.is_authenticated:
            return redirect('desafios-list')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return redirect('login')