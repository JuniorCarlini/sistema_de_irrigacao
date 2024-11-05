from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirecionar para a página principal ou dashboard
            return redirect('dashboard')  # Ajuste a URL conforme necessário
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'users/html/login.html')

def about_view(request):
    return render(request, 'about/html/about.html')