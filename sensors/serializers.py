from rest_framework import serializers
from .models import DataCollection, SolenoidState, StatusFertil, StoricFertil

class SolenoidStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolenoidState
        fields = ['is_open']

class DataCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataCollection
        fields = ['temperature', 'air_humidity', 'soil_humidity']

class StartFertilSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusFertil
        fields = ['start_fertil']

class StoricFertilSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoricFertil
        fields = ['data_fertil_irrigacao']
