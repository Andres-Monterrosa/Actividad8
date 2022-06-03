from django.contrib import admin
from .models import *
# Register your models here.


class MenbeShip(admin.TabularInline):
    model = VehiculoVenta
    extra = 1


class VentaAdmin(admin.ModelAdmin):
    inlines = (MenbeShip,)


admin.site.register(Venta, VentaAdmin)
