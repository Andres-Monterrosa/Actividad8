from django import forms
from apps.vehiculo.models import Vehiculo

class Vehiculoform(forms, Vehiculo):

    class Meta:
        model = Vehiculo

        fields = [
            'modelo',
            'color',
            'placa',
            'motor',
            'marca',
            'tipovehiculo',
        ]

         labels = {
            'modelo': 'Ingrese el Modelo',
            'color': 'Ingrese el Color',
            'placa': 'Ingrese la Placa',
            'motor: ': 'Ingrese el Motor',
            'marca': 'Ingrese la Marca',
            'tipovehiculo': 'Ingrese Tipo vehiculo',
        }

        