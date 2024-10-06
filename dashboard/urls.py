from django.urls import path
from .views import dashboard_view, configuration_view, get_water_usage_data, get_data_collection_data

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('configuration/', configuration_view, name='configuration'),
    path('get-water-usage/', get_water_usage_data, name='get_water_usage_data'),
    path('get-data-collection/', get_data_collection_data, name='get_data_collection_data'),
]
