from django.shortcuts import redirect, render
from django.views.generic import ListView

from pryvehiculos.apps.vehiculo.formVehiculo import Vehiculoform
from .models import Vehiculo
# Create your views here.


class ListviewVehiculos(ListView):
    model = Vehiculo
    template_name = 'vehiculos/vehiculo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehiculos'] = Vehiculo.objects.all().order_by('-id')
        return context

    def vehiculoCreate (request):
        if request.method == 'POST':
            form = Vehiculoform(request.POST)
            if form.is_valid():
                form.save()
            return redirect('vehiculo:listVehiculos')
        else:
            form=Vehiculoform()
            return render(request, 'vehiculos/vehiculo_form.html', {'form': form})