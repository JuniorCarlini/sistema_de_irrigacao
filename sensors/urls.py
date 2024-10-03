from django.urls import path
from .views import collect_environmental_data, collect_solenoid_state

urlpatterns = [
    path('collect-data/', collect_environmental_data, name='collect_environmental_data'),
    path('collect-solenoid-state/', collect_solenoid_state, name='collect_solenoid_state'),
]
