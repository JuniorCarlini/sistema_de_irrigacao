from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                # Busca o usuário no banco de dados
                user = User.objects.get(name=username, password=password)
                # Autenticação bem-sucedida
                messages.success(request, f"Bem-vindo, {user.name}!")
                return redirect('dashboard')  # Redireciona para a página inicial ou dashboard
            except User.DoesNotExist:
                messages.error(request, "Usuário ou senha incorretos.")
        else:
            messages.error(request, "Por favor, preencha o formulário corretamente.")
    else:
        form = LoginForm()

    return render(request, 'users/html/login.html', {'form': form})
