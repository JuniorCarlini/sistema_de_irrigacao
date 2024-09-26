from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField()
    air_humidity = models.FloatField()
    soil_humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Temp: {self.temperature}, Air Humidity: {self.air_humidity}, Soil Humidity: {self.soil_humidity}"
