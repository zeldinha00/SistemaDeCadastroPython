from django.shortcuts import render
from .models import Usuario  #importar o model usuario criado

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # salvar os dados da tela no banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # exibir todos dados em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # retornar os dados para a pagina 
    return render(request, 'usuarios/usuarios.html', usuarios)

