from datetime import timedelta
from rest_framework import status
from django.utils import timezone
from django.shortcuts import render
from .decorators import token_required
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from .models import DataCollection, SolenoidState , WaterUsage, StatusFertil, StoricFertil
from .serializers import DataCollectionSerializer, SolenoidStateSerializer, StartFertilSerializer, StoricFertilSerializer

@api_view(['POST'])
@token_required  # Aplica o decorator para verificar o token
def collect_environmental_data(request):
    serializer = DataCollectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Salva os dados de temperatura, umidade do ar e umidade do solo
        return Response({"status": "success", "message": "Dados ambientais recebidos com sucesso!"}, status=status.HTTP_201_CREATED)
    return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@token_required  # Aplica o decorator para verificar o token
def collect_solenoid_state(request):
    serializer = SolenoidStateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Salva o estado do solenóide
        return Response({"status": "success", "message": "Estado do solenóide recebido com sucesso!"}, status=status.HTTP_201_CREATED)
    return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@token_required  # Aplica o decorator para verificar o token
def collect_historico_fertil(request):
    # Deserializa os dados do request para StoricFertil
    serializer = StoricFertilSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Salva o histórico de irrigação
        return Response({"status": "success", "message": "Histórico de irrigação recebido com sucesso!"}, status=status.HTTP_201_CREATED)
    return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@token_required
def get_data_fertil_state(request):
    status_fertil = StatusFertil.objects.first()

    if status_fertil:
        # Atualiza o status fértil
        status_fertil.atualizar_status()
        
        # Serializa a instância atualizada
        serializer = StartFertilSerializer(status_fertil)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "message": "StatusFertil não encontrado."}, status=status.HTTP_404_NOT_FOUND)

@login_required
def temperature_chart(request):
    # Obtem os dados da URL, se disponíveis
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    hora_inicio = request.GET.get('hora_inicio')
    hora_fim = request.GET.get('hora_fim')

    # Verifica se todos os filtros de data/hora foram fornecidos
    if data_inicio and data_fim and hora_inicio and hora_fim:
        try:
            # Combina data e hora em um único timestamp
            start_datetime = timezone.datetime.fromisoformat(f"{data_inicio} {hora_inicio}")
            end_datetime = timezone.datetime.fromisoformat(f"{data_fim} {hora_fim}")

            # Converte de UTC para o horário local do navegador
            # Usando o timezone local do Django
            start_datetime = timezone.make_aware(start_datetime)
            end_datetime = timezone.make_aware(end_datetime)

            # Filtra os dados no banco de dados
            data = DataCollection.objects.filter(timestamp__range=[start_datetime, end_datetime]).order_by('timestamp')
        except ValueError:
            return HttpResponseBadRequest("Data ou hora em formato inválido.")
    else:
        # Pega os últimos 20 registros por padrão
        data = DataCollection.objects.all().order_by('-timestamp')[:20]

    # Converte os timestamps para o horário local antes de exibi-los
    context = {
        'labels': [timezone.localtime(d.timestamp).strftime('%d-%m-%Y %H:%M') for d in data],
        'temperature_data': [d.temperature for d in data],
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'hora_inicio': hora_inicio,
        'hora_fim': hora_fim,
    }
    return render(request, 'sensors/html/temperature_chart.html', context)

@login_required
def air_humidity_chart(request):
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    hora_inicio = request.GET.get('hora_inicio')
    hora_fim = request.GET.get('hora_fim')

    if data_inicio and data_fim and hora_inicio and hora_fim:
        try:
            start_datetime = timezone.datetime.fromisoformat(f"{data_inicio} {hora_inicio}")
            end_datetime = timezone.datetime.fromisoformat(f"{data_fim} {hora_fim}")

            # Converte de UTC para o horário local do navegador
            # Usando o timezone local do Django
            start_datetime = timezone.make_aware(start_datetime)
            end_datetime = timezone.make_aware(end_datetime)

            # Filtra os dados no banco de dados
            data = DataCollection.objects.filter(timestamp__range=[start_datetime, end_datetime]).order_by('timestamp')
        except ValueError:
            return HttpResponseBadRequest("Data ou hora em formato inválido.")
    else:
        # Pega os últimos 20 registros por padrão
        data = DataCollection.objects.all().order_by('-timestamp')[:20]

    context = {
        'labels': [timezone.localtime(d.timestamp).strftime('%d-%m-%Y %H:%M') for d in data],
        'air_humidity_data': [d.air_humidity for d in data],
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'hora_inicio': hora_inicio,
        'hora_fim': hora_fim,
    }

    return render(request, 'sensors/html/air_humidity_chart.html', context)

@login_required
def soil_humidity_chart(request):
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    hora_inicio = request.GET.get('hora_inicio')
    hora_fim = request.GET.get('hora_fim')

    if data_inicio and data_fim and hora_inicio and hora_fim:
        try:
            start_datetime = timezone.datetime.fromisoformat(f"{data_inicio} {hora_inicio}")
            end_datetime = timezone.datetime.fromisoformat(f"{data_fim} {hora_fim}")

            # Converte de UTC para o horário local do navegador
            # Usando o timezone local do Django
            start_datetime = timezone.make_aware(start_datetime)
            end_datetime = timezone.make_aware(end_datetime)

            # Filtra os dados no banco de dados
            data = DataCollection.objects.filter(timestamp__range=[start_datetime, end_datetime]).order_by('timestamp')
        except ValueError:
            return HttpResponseBadRequest("Data ou hora em formato inválido.")
    else:
        # Pega os últimos 20 registros por padrão
        data = DataCollection.objects.all().order_by('-timestamp')[:20]

    context = {
        'labels': [timezone.localtime(d.timestamp).strftime('%d-%m-%Y %H:%M') for d in data],
        'soil_humidity_data': [d.soil_humidity for d in data],
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'hora_inicio': hora_inicio,
        'hora_fim': hora_fim,
    }

    return render(request, 'sensors/html/soil_humidity_chart.html', context)

@login_required
def water_usage_view(request):
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    hora_inicio = request.GET.get('hora_inicio')
    hora_fim = request.GET.get('hora_fim')

    if data_inicio and data_fim and hora_inicio and hora_fim:
        try:
            start_datetime = timezone.datetime.fromisoformat(f"{data_inicio} {hora_inicio}")
            end_datetime = timezone.datetime.fromisoformat(f"{data_fim} {hora_fim}")

            # Converte de UTC para o horário local do Django
            start_datetime = timezone.make_aware(start_datetime)
            end_datetime = timezone.make_aware(end_datetime)

            # Filtra os dados no banco de dados
            water_usages = WaterUsage.objects.filter(timestamp__range=[start_datetime, end_datetime]).order_by('timestamp')
        except ValueError:
            return HttpResponseBadRequest("Data ou hora em formato inválido.")
    else:
        # Pega os últimos 20 registros por padrão
        water_usages = WaterUsage.objects.all().order_by('-timestamp')[:20]

    # Extraindo dados
    water_usage_data = [round(usage.water_used, 2) for usage in water_usages]
    labels = [timezone.localtime(usage.timestamp).strftime('%d-%m-%Y %H:%M') for usage in water_usages]

    context = {
        'water_usage_data': water_usage_data,
        'labels': labels,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'hora_inicio': hora_inicio,
        'hora_fim': hora_fim,
    }

    return render(request, 'sensors/html/use_water_chart.html', context)

@login_required
def fertil_usage_view(request):
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    hora_inicio = request.GET.get('hora_inicio')
    hora_fim = request.GET.get('hora_fim')

    if data_inicio and data_fim and hora_inicio and hora_fim:
        try:
            # Cria objetos datetime a partir dos dados fornecidos
            start_datetime = timezone.datetime.fromisoformat(f"{data_inicio} {hora_inicio}")
            end_datetime = timezone.datetime.fromisoformat(f"{data_fim} {hora_fim}")

            # Converte para o horário local do Django
            start_datetime = timezone.make_aware(start_datetime)
            end_datetime = timezone.make_aware(end_datetime)

            # Filtra os dados no banco de dados
            fertil_usages = StoricFertil.objects.filter(data_fertil_irrigacao__range=[start_datetime, end_datetime]).order_by('data_fertil_irrigacao')
        except ValueError:
            return HttpResponseBadRequest("Data ou hora em formato inválido.")
    else:
        # Pega os últimos 20 registros por padrão
        fertil_usages = StoricFertil.objects.all().order_by('-data_fertil_irrigacao')[:20]

    # Extraindo dados para o gráfico
    irrigation_data = [1 for _ in fertil_usages]  # Cada evento de irrigação conta como 1
    labels = [timezone.localtime(usage.data_fertil_irrigacao).strftime('%d-%m-%Y %H:%M') for usage in fertil_usages]

    # Passa os dados para o contexto do template
    context = {
        'irrigation_data': irrigation_data,
        'labels': labels,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'hora_inicio': hora_inicio,
        'hora_fim': hora_fim,
    }

    return render(request, 'sensors/html/uso_fertil_chart.html', context)
