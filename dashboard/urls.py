from django.urls import path
from .views import dashboard_view , configuration_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('configuration/', configuration_view, name='configuration'),
]
