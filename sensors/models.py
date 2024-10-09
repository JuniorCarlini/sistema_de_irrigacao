from django.db import models
from django.utils import timezone

class FlowRate(models.Model):
    rate = models.FloatField()

    def __str__(self):
        return f"Flow rate: {self.rate} L/min"

class SolenoidState(models.Model):
    is_open = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solenoid is {'open' if self.is_open else 'closed'} at {self.timestamp}"

    def save(self, *args, **kwargs):
        # Verifique se estamos fechando o solenóide
        if not self.is_open:
            # Obtém a última instância aberta
            last_open_state = SolenoidState.objects.filter(is_open=True).order_by('-timestamp').first()

            if last_open_state:
                # Calcula a duração que o solenóide ficou aberto
                duration = timezone.now() - last_open_state.timestamp
                duration_in_seconds = duration.total_seconds()

                # Obtenha a última taxa de fluxo em litros por minuto
                flow_rate_instance = FlowRate.objects.order_by('-id').first()
                flow_rate_lpm = flow_rate_instance.rate if flow_rate_instance else 30.0  # Default to 30 L/min if no rate is found

                # Converter a taxa de fluxo de L/min para L/s
                flow_rate_lps = flow_rate_lpm / 60.0

                # Calcular a água usada
                water_used = flow_rate_lps * duration_in_seconds

                # Salva o uso da água no modelo WaterUsage
                WaterUsage.objects.create(solenoid_state=last_open_state, water_used=water_used)

        #salva o estado atual
        super().save(*args, **kwargs)

class WaterUsage(models.Model):
    solenoid_state = models.ForeignKey(SolenoidState, on_delete=models.CASCADE, related_name='water_usages')
    water_used = models.FloatField()  # Gasto de água em litros
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Water used: {self.water_used} L at {self.timestamp}"

class DataCollection(models.Model):
    temperature = models.FloatField()
    air_humidity = models.FloatField()
    soil_humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data: Temp={self.temperature}, Air Humidity={self.air_humidity}, Soil Humidity={self.soil_humidity}"

class Configuracao(models.Model):
    token = models.CharField(max_length=255)

    def __str__(self):
        return f"Configuração: {self.token}"