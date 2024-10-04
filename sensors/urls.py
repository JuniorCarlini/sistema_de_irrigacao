from django.urls import path
from .views import collect_environmental_data, collect_solenoid_state, temperature_chart, air_humidity_chart, soil_humidity_chart, water_usage_view

urlpatterns = [
    path('collect-data/', collect_environmental_data, name='collect_environmental_data'),
    path('collect-solenoid-state/', collect_solenoid_state, name='collect_solenoid_state'),
    path('temperature-chart/', temperature_chart, name='temperature_chart'),
    path('air-humidity-chart/', air_humidity_chart, name='air_humidity_chart'),
    path('soil-humidity-chart/', soil_humidity_chart, name='soil_humidity_chart'),
    path('water-usage/', water_usage_view, name='water_usage_view'),
]