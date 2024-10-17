import secrets
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sensors.models import WaterUsage, DataCollection, FlowRate, Configuracao, ConfigFertil, TimeFerti

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
    flow_rate_instance, _ = FlowRate.objects.get_or_create(id=1, defaults={'rate': 0.0})
    configuracao_instance, _ = Configuracao.objects.get_or_create(id=1, defaults={'token': ''})
    config_fertil_instance, _ = ConfigFertil.objects.get_or_create(id=1, defaults={'time_fertil': 1})
    time_ferti_instance, _ = TimeFerti.objects.get_or_create(id=1, defaults={'time_ferti_ms': 0})

    if request.method == 'POST':
        # Atualização da taxa de fluxo
        if 'update_flow_rate' in request.POST:
            new_rate = request.POST.get('flow_rate')
            if new_rate:
                flow_rate_instance.rate = float(new_rate)
                flow_rate_instance.save()
            else:
                print("O valor de flow_rate não foi enviado corretamente.")

        # Atualização do ciclo de fertil
        if 'time_fertil' in request.POST:
            new_time_fertil = request.POST.get('time_fertil')
            config_fertil_instance.time_fertil = int(new_time_fertil)
            config_fertil_instance.save()

        # Atualização do tempo da bomba de fertilização
        if 'update_time_fertil' in request.POST:
            new_time_ferti_ms = request.POST.get('time_ferti_ms')
            if new_time_ferti_ms:  # Verifica se new_time_ferti_ms não é None
                time_ferti_instance.time_ferti_ms = int(new_time_ferti_ms)
                time_ferti_instance.save()
            else:
                print("O valor de time_ferti_ms não foi enviado corretamente.")

        # Geração de novo token
        if 'generate_token' in request.POST:
            new_token = secrets.token_hex(16)
            configuracao_instance.token = new_token
            configuracao_instance.save()

        return redirect('configuration')
        

    return render(request, 'configuration/html/configuration.html', {
        'flow_rate': flow_rate_instance,
        'configuracao': configuracao_instance,
        'config_fertil': config_fertil_instance,
        'time_ferti': time_ferti_instance,
    })
