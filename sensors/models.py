from django.db import models

class SolenoidState(models.Model):
    is_open = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solenoid is {'open' if self.is_open else 'closed'} at {self.timestamp}"

class DataCollection(models.Model):
    temperature = models.FloatField()
    air_humidity = models.FloatField()
    soil_humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data: Temp={self.temperature}, Air Humidity={self.air_humidity}, Soil Humidity={self.soil_humidity}"
