from sensors.models import FlowRate
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/html/dashboard.html')

@login_required
def configuration_view(request):
    # Busca ou cria uma instância de FlowRate, garantindo que sempre exista uma
    flow_rate_instance, created = FlowRate.objects.get_or_create(id=1, defaults={'rate': 0.0})

    if request.method == 'POST':
        # Obtém a nova taxa de fluxo do formulário
        new_rate = request.POST.get('flow_rate')

        # Atualiza a taxa de fluxo com o valor submetido
        flow_rate_instance.rate = float(new_rate)
        flow_rate_instance.save()

        return redirect('configuration')  # Redireciona para evitar o reenvio do formulário
    print(flow_rate_instance)
    return render(request, 'configuration/html/configuration.html', {'flow_rate': flow_rate_instance})
