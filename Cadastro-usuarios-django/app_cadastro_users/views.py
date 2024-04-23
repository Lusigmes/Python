from django.shortcuts import render
from .models import User

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def users(request):
    #Salvar
    novo_user = User()
    novo_user.nome = request.POST.get('nome')
    novo_user.idade = request.POST.get('idade')
    novo_user.save()
    #exibir users cadastrados na nova pag
    users = {
        'users': User.objects.all()
    }
    #retorna dados para pagina de listagem
    return render(request, 'users/users.html', users)