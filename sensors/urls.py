from django.urls import path
from .views import collect_environmental_data, collect_solenoid_state, temperature_chart, air_humidity_chart, soil_humidity_chart, water_usage_view, fertil_usage_view, get_data_fertil_state, collect_historico_fertil

urlpatterns = [
    path('collect-data/', collect_environmental_data, name='collect_environmental_data'),
    path('collect-solenoid-state/', collect_solenoid_state, name='collect_solenoid_state'),
    path('temperature-chart/', temperature_chart, name='temperature_chart'),
    path('air-humidity-chart/', air_humidity_chart, name='air_humidity_chart'),
    path('soil-humidity-chart/', soil_humidity_chart, name='soil_humidity_chart'),
    path('water-usage/', water_usage_view, name='water_usage_view'),
    path('fertil-usage/', fertil_usage_view, name='fertil_usage_view'),
    path('data-fertil_state/', get_data_fertil_state, name='get_data_fertil_state'),
    path('historico-fertil/', collect_historico_fertil, name='collect_historico_fertil'),
]