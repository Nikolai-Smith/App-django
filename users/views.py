from django.shortcuts import redirect, render
from .models import User #importa a classe do models
from .forms import UserForm
# Create your views here.
def listar_users(request):
    users = User.objects.all() #recebe tudo da classe na variavel users
    return render(request, 'users/listar_users.html', {'users': users}) #passa a variavel para o dicionario ser usado na template

def cadastrar_users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_users')
    else:
        form = UserForm()
    return render(request, 'users/criarconta.html', {'form': form})

def listar_user_id(request, id):
    user = User.objects.get(id=id)
    return render(request, 'users/lista_users.html', {'user':user})

def editar_user(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('listar_users')
    return render(request, 'users/criarconta.html', {'form': form})


def remover_user(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('listar_users')
    return render(request, 'users/confirma_exclusao.html', {'user': user})



