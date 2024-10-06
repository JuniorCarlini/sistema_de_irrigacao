from sensors.models import FlowRate
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from sensors.models import WaterUsage, DataCollection
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/html/dashboard.html')

@login_required
def get_water_usage_data(request):
    water_usages = WaterUsage.objects.all().order_by('-timestamp')[:10]  # Últimos 10 registros
    data = {
        'labels': [usage.timestamp.strftime('%d-%m-%Y %H:%M') for usage in water_usages],
        'water_used': [round(usage.water_used, 2) for usage in water_usages],
    }
    return JsonResponse(data)
    print(data)

@login_required
def get_data_collection_data(request):
    latest_data = DataCollection.objects.latest('timestamp')
    data = {
        'temperature': round(latest_data.temperature, 2),
        'air_humidity': round(latest_data.air_humidity, 2),
        'soil_humidity': round(latest_data.soil_humidity, 2),
    }
    return JsonResponse(data)


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
