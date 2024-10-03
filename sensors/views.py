from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DataCollection, SolenoidState
from .serializers import DataCollectionSerializer, SolenoidStateSerializer

@api_view(['POST'])
def collect_environmental_data(request):
    if request.method == 'POST':
        serializer = DataCollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Salva os dados de temperatura, umidade do ar e umidade do solo
            return Response({"status": "success", "message": "Dados ambientais recebidos com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def collect_solenoid_state(request):
    if request.method == 'POST':
        serializer = SolenoidStateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Salva o estado do solenóide
            return Response({"status": "success", "message": "Estado do solenóide recebido com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
