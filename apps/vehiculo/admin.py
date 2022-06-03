from django.contrib import admin
from .models import *
# Register your models here.

class VehiculosAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'color', 'placa',
                    'motor', 'marca', 'tipoVehiculo']
    ordering = ['motor']
    list_filter = ('modelo', 'marca')
    search_fields = ['placa', 'color']


class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre']


class TipoVehiculosAdmin(admin.ModelAdmin):
    list_display = ['nombre']


admin.site.register(Marca, MarcaAdmin)
admin.site.register(TipoVehiculo, TipoVehiculosAdmin)
admin.site.register(Vehiculo, VehiculosAdmin)