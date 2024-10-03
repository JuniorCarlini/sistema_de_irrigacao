from rest_framework import serializers
from .models import DataCollection, SolenoidState

class SolenoidStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolenoidState
        fields = ['is_open']

class DataCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataCollection
        fields = ['temperature', 'air_humidity', 'soil_humidity']
