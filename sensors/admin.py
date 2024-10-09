from django.contrib import admin
from .models import SolenoidState, DataCollection, FlowRate, WaterUsage, Configuracao

admin.site.register(SolenoidState)
admin.site.register(DataCollection)
admin.site.register(FlowRate)
admin.site.register(WaterUsage)
admin.site.register(Configuracao)