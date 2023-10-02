from typing import Any
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Vehicle, Location
from django.views.generic.edit import CreateView


class Home(LoginView):
    fields = '__all__'
    template_name = 'home.html'


class AddVehicle(CreateView):
    model = Vehicle
    fields = ['year', 'make', 'model', 'msrp', 'color', 'notes', 'engine', 'odometer', 'interior', 'transmission' , 'condition',
    'vehicle_type', 'location', 'image']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Vehicle'
        return context

def vehicle_index(request):
    vehicles = Vehicle.objects.all()

    return render(request, 'vehicles/index.html', {
        'vehicles': vehicles,
        'title': 'Vehicle List'
    })
