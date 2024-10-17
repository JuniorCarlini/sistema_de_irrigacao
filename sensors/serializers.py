from rest_framework import serializers
from .models import DataCollection, SolenoidState, StatusFertil, StoricFertil, TimeFerti

class SolenoidStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolenoidState
        fields = ['is_open']

class DataCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataCollection
        fields = ['temperature', 'air_humidity', 'soil_humidity']

class StoricFertilSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoricFertil
        fields = ['data_fertil_irrigacao']

class CombinedSerializer(serializers.Serializer):
    time_ferti_ms = serializers.IntegerField()
    start_fertil = serializers.BooleanField()

    def to_representation(self, instance):
        # Obtém os dados de TimeFerti e StatusFertil
        time_ferti = TimeFerti.objects.first()
        status_fertil = StatusFertil.objects.first()

        if time_ferti and status_fertil:
            return {
                'time_ferti_ms': time_ferti.time_ferti_ms,
                'start_fertil': status_fertil.start_fertil,
            }
        else:
            return {
                'time_ferti_ms': None,
                'start_fertil': None,
            }
