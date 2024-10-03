from django.contrib import admin
from .models import SolenoidState, DataCollection

admin.site.register(SolenoidState)
admin.site.register(DataCollection)
