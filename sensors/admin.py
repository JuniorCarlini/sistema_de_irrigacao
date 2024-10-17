from django.contrib import admin
from .models import SolenoidState, DataCollection, FlowRate, WaterUsage, Configuracao, StatusFertil , ConfigFertil, StoricFertil

admin.site.register(SolenoidState)
admin.site.register(DataCollection)
admin.site.register(FlowRate)
admin.site.register(WaterUsage)
admin.site.register(Configuracao)
admin.site.register(StatusFertil)
admin.site.register(ConfigFertil)
admin.site.register(StoricFertil)